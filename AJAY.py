class car:
    def _init_(self):
        self.cgst=5555
        self.sgst=6478
        self.insurance=7567
    def company(self):
        while True:
            print("toyota,mercedes,mahendra")
            self.n=input("enter the car company")
            if self.n=="toyota":
                print("welcome to toyota")
                self.model()
                break
            elif self.n=="mercedes":
                print("welcome to mercedes")
                self.model()
                break
            elif self.n=="mahendra":
                print("welcome to mahendra")
                self.model()
                break
            else:
                print("enter valid company")
    def model(self):
        if self.n=="toyota":
            while True:
                print("select from fortuner and lc")
                self.choice=input("enter the car model")
                if self.choice=="fortuner":
                    self.price(self.choice)
                    break
                elif self.choice=="lc":
                    self.price(self.choice)
                    break
                else:
                    print("enter valid company")
    def model(self):
        if self.n=="mercedes":
            while True:
                print("select from glb and amg")
                self.choice=input("enter the car model")
                if self.choice=="glb":
                    self.price(self.choice)
                    break
                elif self.choice=="amg":
                    self.price(self.choice)
                    break
                else:
                    print("enter valid company")
    def model(self):
        if self.n=="mahendra":
            while True:
                print("select from thar and scorpio")
                self.choice=input("enter the car model")
                if self.choice=="thar":
                    self.price(self.choice)
                    break
                elif self.choice=="scorpio":
                    self.price(self.choice)
                    break
                else:
                    print("enter valid company")
    def price(self,choice):
        if choice=="Fortuner":
            self.p=45000000
        elif choice=="lc":
            self.p=10000000
        elif choice=="amg":
            self.p=4321717
        elif choice=="gw":
            self.p=36387267
        tot_p=self.p+self.cgst+self.sgst+self.insurance
        print(tot_p)
l=car()
l.company()

        