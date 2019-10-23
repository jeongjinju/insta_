# hashtag에 링크를 연결시켜주기 위해서 만듬 
# 함수를 선언하는 것과 같은 역할

from django import template

register = template.Library()


# word 하나하나를 <a>로 감싸주기 위한 함수를 만드는 것
@register.filter
def hashtag_link(post):
    content = post.content
    # 들어가 있는 실제 데이터
    #. #고양이 #야옹 #강아지 #멍멍
    # 바꾸고 싶은 모양>> <a>고양이</a>, ....
    #  replace> str을 str으로 바꾸기
    hashtags = post.hashtags.all()
    # QuerySet [HashTag object(1), ...]
    for hashtag in hashtags:
        # raplace(과거의값(바꿀값), 새로운값(바뀐값))
        # content.replace(#고양이)
        content = content.replace(
            f'{hashtag.content}', 
            f'<a href="posts/hashtags/{hashtag.id}/">{hashtag.content}</a>'
        )
    
    return content