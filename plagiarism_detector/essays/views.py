from django.shortcuts import render, redirect



# Create your views here.

def index(request):
    if request.user.is_authenticated :
        return render(request, 'index.html')
    else :
        return redirect('login')


# def create(request):
#     return render(request, 'form.html', {
#         'title': 'Crear Ensayo',
#         'index': -1
#     })
#
#
# def edit(request, essay_index: int):
#     essay = essays_arr[essay_index - 1]
#     return render(request, 'form.html', {
#         'title': 'Editar Ensayo',
#         'essay': essay,
#         'index': essay_index
#     })
#
#
# def delete(request, essay_index: int):
#     essays_arr.pop(essay_index - 1)
#     return redirect('essays.index')
#
#
# def show(request, essay_index: int):
#     essay = essays_arr[essay_index - 1]
#     return render(request, 'detail.html', {
#         'title': 'Detalle Ensayo',
#         'essay': essay,
#         'index': essay_index
#     })
#
#
# def save(request):
#     pos = int(request.POST['index'])
#     now = datetime.date.today().strftime(' %d-%m-%Y')
#     if pos == -1:
#         essays_arr.append({
#             "title": request.POST['title'],
#             "author": request.POST['author'],
#             "content": request.POST['content'],
#             "date": now
#         })
#     else:
#         essays_arr[pos - 1] = {
#             "title": request.POST['title'],
#             "author": request.POST['author'],
#             "content": request.POST['content'],
#             "date": now
#         }
#     return redirect('essays.index')
