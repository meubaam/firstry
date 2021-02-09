from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from fcuser.models import Fcuser
from tag.models import Tag
from django.http import Http404
from .models import Board
from .forms import BoardForm
# Create your views here.

def board_list(request):
    all_boards = Board.objects.all().order_by('-id') #-id 시간 역순- 즉 가장 최신 글을 먼저 보겠다는 뜻.
    page = request.GET.get('p',1)
    paginator = Paginator(all_boards, 5)

    boards = paginator.get_page(page)

    return render(request, 'board_list.html', {'boards': boards}) 

def board_detail(request, pk):
    try :
        board = Board.objects.get(pk=pk)
    except Board.DoesNotExist:
        raise Http404('The requested post cannot be found')

    return render(request, 'board_detail.html', {'board': board})

def board_write(request):
    if not request.session.get('user'):
        return redirect('/fcuser/login/')

    if  request.method == 'POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            user_id = request.session.get('user')
            fcuser = Fcuser.objects.get(pk=user_id)

            tags = form.cleaned_data['tags'].split(',')

            board = Board()
            board.title = form.cleaned_data['title']
            board.contents = form.cleaned_data['contents']
            board.writer = fcuser
            board.save()

            for tag in tags:
                if not tag:
                    continue

                else:
                 _tag, _ = Tag.objects.get_or_create(name=tag)
                board.tags.add(_tag)

        return redirect('/board/list/')            
    
    else :
        form = BoardForm()

    return render(request, 'board_write.html', {'form':form})