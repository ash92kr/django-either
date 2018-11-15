from django.shortcuts import render, redirect, resolve_url
from question.forms import QuestionForm, CommentForm   # QuestionForm class를 가져옴
from .models import Question
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib.auth.decorators import login_required

# Create your views here.
def list(request):
    # questions = Question.objects.all()  # 전체 목록을 보여주는 코드 -> 모든 질문을 가져옴
    questions_list = Question.objects.all()
    paginator = Paginator(questions_list, 5)  # 페이지 당 5개씩 끊음

    page = request.GET.get('page')
    questions = paginator.get_page(page)
    # return render(request, 'list.html', {'contacts': contacts})
    
    return render(request, 'question/list.html', {'questions':questions})  # 자동으로 감지하지 못하고 설정 필요

@login_required
def create(request):   # 에러 페이지의 모든 데이터는 request에 저장되어 전달된다
    if request.method == "POST":
        # 데이터를 저장하는 로직 - post 방식으로 넘어와야 데이터를 DB에 저장
        form = QuestionForm(request.POST)   # 사용자가 입력한 내용을 폼에 넣어 저장
        if form.is_valid():   # 빈 데이터나 형식에 맞지 않는지 검증
            question = form.save(commit=False)
            question.user = request.user  # user 정보(로그인이 된 사람만 가능)
            question.save()
            return redirect(resolve_url('question:list'))
    else:  # GET 방식
        # 사용자에게 폼을 만들어 전달
        form = QuestionForm()   # 웹페이지가 직접 폼 내용을 자동으로 담아 건네줌
    return render(request, 'question/create.html', {'form': form})

@login_required
def detail(request, id):
    question = Question.objects.get(id=id)
    form = CommentForm(initial={'question':id})  # question의 값을 id로 넘김 -> 특정 title에 대한 댓글을 달아 넘길 수 있음
    A = question.comment_set.all().filter(answer="A")
    B = question.comment_set.all().filter(answer="B")
    
    if len(A) + len(B) == 0:
        A_per = 0
        B_per = 0
    else:
        A_per = len(A) / (len(A) + len(B)) * 100
        B_per = len(B) / (len(A) + len(B)) * 100
    
    return render(request, 'question/detail.html', {'question': question, 'form': form, 'A': A, 'B': B, 'A_per':A_per, 'B_per':B_per})
    
    
def comment_create(request, id):
    if request.method == "POST":
        # 저장하기
        form = CommentForm(request.POST)  # request.POST에 사용자가 입력한 정보 저장됨
        if form.is_valid():
            comment = form.save(commit=False)  # save는 add와 commit이 가능한데, add만 가능
            comment.question = Question.objects.get(id=id)  # id 베이스로 Question을 찾고 comment.question에 저장
            comment.save()
            return redirect(resolve_url('question:detail', id))   # 댓글을 단 title 페이지 보여주기
        
    else:  # GET 방식 요청
        # form = CommentForm()  # comment만 만드는 페이지가 없어 detail로 연결 - 문제는 comment만 넣는 페이지가 없어 redirect함
        return redirect(resolve_url('question:detail', id))
    return render(request, 'question/detail.html', {'form':form})


def update(request, id):
    question = Question.objects.get(id=id)
    
    if request.method == 'POST':
        # 업데이트 로직
        form = QuestionForm(request.POST, instance=question)  # instance와 비교해 POST를 통해 바꾸기
        if form.is_valid():
            form.save()
            return redirect(resolve_url('question:detail', id))
    else:
        # 폼 보여주기
        form = QuestionForm(instance=question)  # 사용자가 기존에 넣었던 데이터를 출력함
    return render(request, 'question/update.html', {'form':form, 'question':question})
    
def delete(request, id):
    question = Question.objects.get(id=id)
    question.delete()
    return redirect(resolve_url('question:list'))


# def comment_update(request, id):
#     comment = Comment.objects.get(id=id)

#     if request.method == "POST":
#         form = CommentForm(request.POST, instance=comment)
#         if comment.is_valid():
#             comment.save
#             return redirect(resolve_url('comment:detail', id))
#     else:
#         form = CommentForm(instance=comment)
#     return render(request, 'question/update.html', {'comment':comment})


# def comment_delete(request, id):
#     comment = Comment.objects.get(id=id)
#     comment.delete()
#     return redirect(resolve_url('comment:list'))
    