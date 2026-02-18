from django.http import HttpResponse
from .models import TextRecord

def add(request):
    text = request.GET.get("text", "").strip()
    if not text:
        text = "Sample text inserted from /add"

    TextRecord.objects.create(text=text)

    return HttpResponse(
        f"✅ Added: <b>{text}</b><br><br>"
        f"Go to <a href='/show'>/show</a>"
    )

def show(request):
    records = TextRecord.objects.all().order_by("-id")

    if not records.exists():
        return HttpResponse("No records yet. Go to <a href='/add'>/add</a>")

    html = "<h2>Stored Records</h2><ul>"
    for r in records:
        html += f"<li>{r.id}: {r.text}</li>"
    html += "</ul><br><a href='/add'>Add another</a>"

    return HttpResponse(html)
