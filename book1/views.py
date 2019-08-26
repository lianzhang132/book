from django.shortcuts import render,HttpResponse,redirect
from book1.models import *

def search(request):
    return HttpResponse("哈哈")

def authoradd(request):
    authors= Auther(nid=2,name="老舍",age=20,authorinfo_id=2)
    authors.save()
    return HttpResponse("ok")
def publicadd(request):
    # publics= Public_info(nid=1,name="人民出版社",city="北京",email="157482547@qq.com")
    # publics= Public_info(nid=2,name="达摩院出版社",city="郑州",email="9865747@qq.com")
    publics= Public_info(nid=3,name="科教出版社",city="深圳",email="huayu@qq.com")
    publics.save()
    return HttpResponse("ok")
def lists(request):
    # bookojbk=Book.objects.filter(title="钢铁").first()
    # bookobj=Book.objects.filter(title="c#速成").first()

    # yuguangzhong=Auther.objects.filter(name="余光中").first()
    # laoshe=Auther.objects.filter(name="老舍").first()
    # bookobj.authers.add(yuguangzhong,laoshe)
    # bookobj = Book.objects.filter(nid=7).first()
    # bookobj.authers.remove(1)
    # bookobj = Book.objects.filter(nid=3).first()
    # bookobj = Book.objects.filter(title="c#速成").all().clear()
    # bookobj.authers.remove(1)
    # publics = Public_info.objects.filter(name="达摩院出版社").first()
    # print(publics.book_set.all())
    # publics = Public_info.objects.filter(book__title="简爱").values("name")
    # publics = Book.objects.filter(title="简爱").values("public__name")
    # publics = Book.objects.filter(title="简爱").values("authers__name")
    # autuers = Auther.objects.filter(book__title="路遥").values("name")
    # res = Auther.objects.filter(name="鲁迅").values("authorinfo__telephone")
    # res = Auther_info.objects.filter(auther__name="鲁迅").values("telephone")
    #第一个authers对应models中的类名 第二个是类中的外键 第三个是外键对应类的属性 第四个是方法
    # res = Book.objects.filter(authers__authorinfo__telephone__startswith="15").values("title","public__name")
    # res = Auther.objects.filter(authorinfo__telephone__startswith="15").values("book__title","book__public__name")
    from django.db.models import Avg,Max,Min,Count
    # res= Book.objects.all().aggregate(avgprice=Avg("price"),maxprice=Max("price"))
    # res= Auther.objects.all().aggregate(avgprice=Avg("authorinfo__cost"),maxprice=Max("authorinfo__salary"))
    # res= Auther.objects.values("authorinfo__age").annotate(minsalary=Min("authorinfo__salary")).values("name","minsalary")
    # res=Public_info.objects.values("nid").annotate(num=Count("book__title"))
    # res=Public_info.objects.values("name").annotate(num=Count("book__title"))
    # res=Public_info.objects.values("nid").annotate(num=Count("book__title")).values("name","num")
    # res=Auther.objects.values("nid").annotate(maxprice=Max("book__price")).values("name","maxprice")
    # res=Book.objects.values("nid").annotate(su=Count("authers__name")).values("title","su")
    # res=Book.objects.filter(title__startswith="p").values("pk").annotate(con=Count("authers__nid")).values("title","con")
    # res=Book.objects.annotate(con=Count("authers__nid")).filter(con__gt=1).values("title","con")
    from django.db.models import F,Q
    # res=Auther_info.objects.filter(cost__gt=F("salary")).values("salary")
    # print(res)
    # Auther_info.objects.update(salary=F("salary")+5000)
    # res = Book.objects.filter((Q(title="简爱")&Q(price=200)|Q(price=25)))
    # res = Book.objects.filter((~Q(title="简爱")&Q(price=200)|Q(price=25)))
    res = Book.objects.filter((~Q(title="简爱")|Q(price=200)))

    return HttpResponse(res)

def bookadd(request):
    publiclist=Public_info.objects.all()
    if request.method == 'POST':
        title = request.POST.get('title')
        price = request.POST.get('price')
        pub_date = request.POST.get('pub_date')
        public = request.POST.get('public')
        authorslist = request.POST.getlist('author')
        # nid = Public_info.objects.filter(name=public).values("nid")
        # nid=nid[0]["nid"]
        # anthorlist = author.split(" ")#以空格键分割作者成列表
        res = Book.objects.create(title=title, price=price, pub_date=pub_date, public_id=public)#添加书到列表中
        res.authers.add(*authorslist)
        return redirect("/book1/booklist/")
        # res.save()
        # bookobj = Book.objects.filter(title=title).first()#取出新添加的书
        # newid=bookobj[0]
        #
        #
        # f=Book.objects.filter(title=title).first()
        # m=7
        # for n in authorslist:
        #     auth=Auther(name=n,authorinfo_nid=7)#这里的错 怎么解决？？
        #     n1=Auther.objects.filter(name=n).first()
        #     bookobj.authers.add(n1)
    authorobjli=Auther.objects.all()



        # res2=Auther_info.objects.update()
        # res2=Auther.objects.update(name=)


        # if res:
        #     return redirect('/blog/books_list/')

    # book = Book.objects.filter(id=id).first()
    return render(request, 'bookadd.html',locals())
    # return render(request, "login.html")

    # return HttpResponse("ojbk")
def booklist(request):
    book_list=Book.objects.all()
    return render(request,"booklist.html",locals())
def bookdelete(request,id):
    # return HttpResponse("删除成功")
    Book.objects.filter(pk=id).delete()
    return redirect("/book1/booklist/")
    # return HttpResponse("删除成功")
def bookupdate(request,id):
    book_obj = Book.objects.filter(pk=id).first()

    if request.method == 'POST':
        title = request.POST.get('title')
        price = request.POST.get('price')
        pub_date = request.POST.get('pub_date')
        public = request.POST.get('public')
        authorslist = request.POST.getlist('author')
        # nid = Public_info.objects.filter(name=public).values("nid")
        # nid=nid[0]["nid"]
        # anthorlist = author.split(" ")#以空格键分割作者成列表
        Book.objects.filter(pk=id).update(title=title,price=price,pub_date=pub_date,public_id=public)
        book_obj.authers.clear()
        book_obj.authers.add(*authorslist)
        return redirect("/book1/booklist/")
        # res.save()
        # bookobj = Book.objects.filter(title=title).first()#取出新添加的书
        # newid=bookobj[0]
        #
        #
        # f=Book.objects.filter(title=title).first()
        # m=7
        # for n in authorslist:
        #     auth=Auther(name=n,authorinfo_nid=7)#这里的错 怎么解决？？
        #     n1=Auther.objects.filter(name=n).first()
        #     bookobj.authers.add(n1)
    authorobjli = Auther.objects.all()
    publiclist = Public_info.objects.all()

    # res2=Auther_info.objects.update()
    # res2=Auther.objects.update(name=)

    # if res:
    #     return redirect('/blog/books_list/')

    # book = Book.objects.filter(id=id).first()
    return render(request, 'bookupdate.html', locals())
    # return render(request, "login.html")

    # return HttpResponse("ojbk")

