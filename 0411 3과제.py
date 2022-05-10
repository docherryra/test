""" 가게에서 사용하는 쇼핑카트 클래스를 제작합니다.
해당 클래스에는 사용할 수 있는 다음의 함수들과 변수가 있습니다.


1. Cart 클래스
변수
1. plist : 담은 물건 리스트
2. name : 구매자명
3. amount : 쇼핑카트에 담은 물건들의 총액


함수
생성자
    쇼핑카트를 하나 생성합니다. 매개 변수 1개(name)을 가지고
    self.name 의 값을 설정해줍니다.
    그 외 plist, amount는 각각 [], 0 로 설정해줍니다

add_product 함수
    쇼핑카트에 물건을 추가합니다. 물건은 product 클래스에서 객체를 생성해 추가합니다.
    물건을 총액을 가진 변수에 product의 getter을 사용해 물건의 총액을 변경합니다.

bill 함수
    plist 에 담긴 상품들의 상품명과 가격을 출력하고, 총액을 함께 출력하세요
    ex)
        사과 : 500
        배: 600
        오렌지 : 300
        -----------
        총액: 1400


getter 함수
각 변수들의 getter를 생성합니다(총 3개).


2. Product 클래스
변수
1. name: 물건 이름
2. price: 물건 가격

함수
생성자
    매개변수 2개를 받아와 물건의 이름과 가격을 설정합니다.
== 중요 ==
Product 클래스의 변수값들에 접근하기 위해서는 항상 getter를 사용해 가져와야 합니다.

"""
class Cart:
    name = ""
    plist = []
    amount = 0

    #변수를 추가하세요


    def __init__(self, name):
        # 함수를 작성하세요
        self.name = name
        self.amount = 0
        self.plist = []

        return

    def add_product(self, product):
        p_name = product.getname()
        p_price = product.getprice()

        self.plist.append([p_name, p_price])
        self.amount += p_price
        print(self.plist)



        # 함수를 작성하세요
        return

    def bill(self):
        for i in self.plist:
            print(i[0],":",  i[1])
        print("----------------------------------")
        print("총액 :", self.amount)
        print()


        # 함수를 작성하세요
        return

    # 변수들의 getter 생성
    def getname(self):
        return self.name


class Product:
    name = ""
    price = ""
    #변수를 추가하세요


    def __init__(self,name,price):
        self.name = name
        self.price = price
        # 함수를 작성하세요
        return

    #변수들의 getter 생성
    def getname(self):
        return self.name

    def getprice(self):
        return self.price


def main(): # 이 함수는 수정하지 않습니다! 테스트용 함수이므로 클래스만 수정해서 원하는 결과값이 나오도록 만들어주세요
    c1 = Cart("파이썬")
    c2 = Cart("두음")
    products_1 = [
        Product("김준혁", 5000000),
        Product("고양이", 10000),
        Product("신입생", 5000001)
    ]
    products_2 = [
        Product("바나나", 2500),
        Product("사과", 1500),
        Product("따듯한 파인애플", 500),
        Product("민트", 250),
        Product("녹차", 2700)
    ]

    for p in products_1:
        c1.add_product(p)

    for p in products_2:
        c2.add_product(p)

    c1.bill()
    c2.bill()


main()