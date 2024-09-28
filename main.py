from tkinter import *

from tkinter import messagebox
import pandas as pd


big_font= ("arial", 16, "bold")

#def use_btn_first_offer_pressed():
#    messagebox.showinfo("use offer","buy 3 books from view window then get another book for free")

#def use_btn_second_offer_pressed():
#    messagebox.showinfo("use offer","buy a television for 15,000 instead of 20,000")

#def use_btn_third_offer_pressed():
#    messagebox.showinfo("use offer","buy any things for more than 500 pounds from view window and"
#                                    "chose any T-shirt without money")

#def use_btn_forth_offer_pressed():
#    messagebox.showinfo("use offer","buy any two shoes and have an offer for 50%"
#                                    " of the third shoes ")

#def use_btn_fifth_offer_pressed():
#    messagebox.showinfo("use offer","buy any things wih more than 1000 pounds then you will "
#                                    "join a lot.....you can win a refrigerator for free")

def use_btn_first_offer_pressed():
    first_offer_window = Tk()

    first_offer_window.title("first offer")

    first_offer_window.geometry("950x500+450+30")

    first_offer_window.config(bg="white")

    offer_name_first_label=Label(first_offer_window,text="The offer is : buy 3 books and have 1 another as a gift",
                           bg="white",fg="black",font=big_font)
    offer_name_first_label.place(x=20,y=100)

    offer_use_first_label=Label(first_offer_window,text="how to use it : buy 3 books from view window then get another book for free",
                           bg="white",fg="black",font=big_font)
    offer_use_first_label.place(x=20,y=300)


def use_btn_third_offer_pressed():
    third_offer_window = Tk()

    third_offer_window.title("third offer")

    third_offer_window.geometry("950x500+450+30")

    third_offer_window.config(bg="white")

    offer_name_third_label=Label(third_offer_window,text="the offer is : buy for more than 500 pounds and have a T-shirt for free",
                           bg="white",fg="black",font=big_font)
    offer_name_third_label.place(x=20,y=100)

    offer_use_third_label=Label(third_offer_window,text="how to use it : buy any things for "
                                                        "more than 500 pounds and "
                                                        "chose any T-shirt for free",
                           bg="white",fg="black",font=big_font)
    offer_use_third_label.place(x=15,y=300)

def use_btn_second_offer_pressed():
    second_offer_window = Tk()

    second_offer_window.title("second offer")

    second_offer_window.geometry("950x500+450+30")

    second_offer_window.config(bg="white")

    offer_name_second_label=Label(second_offer_window,text="The offer is : 25% offer on television",
                           bg="white",fg="black",font=big_font)
    offer_name_second_label.place(x=20,y=100)

    offer_use_second_label=Label(second_offer_window,text="how to use the offer : buy a television for 15,000 instead of 20,000",
                           bg="white",fg="black",font=big_font)
    offer_use_second_label.place(x=20,y=300)

def use_btn_forth_offer_pressed():
    forth_offer_window = Tk()

    forth_offer_window.title("forth offer")

    forth_offer_window.geometry("950x500+450+30")

    forth_offer_window.config(bg="white")

    offer_name_forth_label=Label(forth_offer_window,text="The offer is : buy 2 shoes and have an offer for 50% the third piece",
                           bg="white",fg="black",font=big_font)
    offer_name_forth_label.place(x=20,y=100)

    offer_use_forth_label=Label(forth_offer_window,text="how to use it: buy any two shoes and have an offer "
                                                        "for 50% of the third shoes",
                           bg="white",fg="black",font=big_font)
    offer_use_forth_label.place(x=15,y=300)

def use_btn_fifth_offer_pressed():
    fifth_offer_window = Tk()

    fifth_offer_window.title("fifth offer")

    fifth_offer_window.geometry("950x500+450+30")

    fifth_offer_window.config(bg="white")

    offer_name_fifth_label=Label(fifth_offer_window,text="The offer is : buy for more than 1000 pounds and join a lot on a refrigerator",
                           bg="white",fg="black",font=big_font)
    offer_name_fifth_label.place(x=20,y=100)

    offer_use_fifth_label=Label(fifth_offer_window,text="how to use it : buy any things wih more than 1000 pounds then you will join a lot",
                           bg="white",fg="black",font=big_font)
    offer_use_fifth_label.place(x=15,y=300)

    offer_use_fifth_label2=Label(fifth_offer_window,text="you can win a refrigerator",
                           bg="white",fg="black",font=big_font)
    offer_use_fifth_label2.place(x=15,y=330)


# buy for more than 1000 pounds and join a lot on a refrigerator
#buy any things wih more than 1000 pounds then you will join a lot.....you can win a refrigerator

def sales_btn_pressed():

    sales_window = Tk()

    sales_window.title("sales Product")

    sales_window.geometry("950x500+450+30")

    sales_window.config(bg="#e9f502")

    window.destroy()

    offer_title=Label(sales_window,text="our offers",bg="blue",fg="black",font=mini_font,padx=5,pady=5)
    offer_title.pack()

    first_offer=Label(sales_window,text="buy 3 books and have 1 another as a gift",bg="white",fg="black",font=mini_font,padx=5,pady=5)
    first_offer.place(x=30,y=50)

    second_offer=Label(sales_window,text="25% offer on television",bg="white",fg="black",font=mini_font,padx=5,pady=5)
    second_offer.place(x=30,y=120)

    third_offer=Label(sales_window,text="buy for more than 500 pounds and have a T-shirt for free",bg="white",fg="black",
                      font=mini_font,padx=5,pady=5)
    third_offer.place(x=30,y=190)

    forth_offer=Label(sales_window,text="buy 2 shoes and have an offer for 50% the third piece",bg="white",fg="black",
                      font=mini_font,padx=5,pady=5)
    forth_offer.place(x=30,y=260)

    fifth_offer=Label(sales_window,text="buy for more than 1000 pounds and join a lot on a refrigerator ",bg="white",
                      fg="black",font=mini_font,padx=5,pady=5)
    fifth_offer.place(x=30,y=330)

    num1_offer=Label(sales_window,text="1",bg="green",fg="black",font=mini_font)
    num1_offer.place(x=5,y=52)

    num2_offer=Label(sales_window,text="2",bg="green",fg="black",font=mini_font)
    num2_offer.place(x=5,y=122)

    num3_offer=Label(sales_window,text="3",bg="green",fg="black",font=mini_font)
    num3_offer.place(x=5,y=192)

    num4_offer=Label(sales_window,text="4",bg="green",fg="black",font=mini_font)
    num4_offer.place(x=5,y=262)

    num5_offer=Label(sales_window,text="5",bg="green",fg="black",font=mini_font)
    num5_offer.place(x=5,y=332)

    use_offer_first_btn=Button(sales_window,text="use offer",bg="blue",fg="black",font=mini_font,command=lambda :(use_btn_first_offer_pressed()))
    use_offer_first_btn.place(x=780,y=50)

    use_offer_second_btn = Button(sales_window, text="use offer", bg="blue", fg="black", font=mini_font,
                                 command=lambda: (use_btn_second_offer_pressed()))
    use_offer_second_btn.place(x=780, y=120)

    use_offer_third_btn = Button(sales_window, text="use offer", bg="blue", fg="black", font=mini_font,
                                 command=lambda: (use_btn_third_offer_pressed()))
    use_offer_third_btn.place(x=780, y=190)

    use_offer_forth_btn = Button(sales_window, text="use offer", bg="blue", fg="black", font=mini_font,
                                 command=lambda: (use_btn_forth_offer_pressed()))
    use_offer_forth_btn.place(x=780, y=260)

    use_offer_fifth_btn = Button(sales_window, text="use offer", bg="blue", fg="black", font=mini_font,
                                 command=lambda: (use_btn_fifth_offer_pressed()))
    use_offer_fifth_btn.place(x=780, y=330)


def add_product(product_name, product_price, product_desc,product_code, product_amount,add_window):
    name = product_name.get("1.0", "end-1c")
    price = product_price.get("1.0", "end-1c")
    desc = product_desc.get("1.0", "end-1c")
    code = product_code.get("1.0", "end-1c")
    amount = product_amount.get("1.0", "end-1c")
    print(name)
    print(price)
    print(desc)
    print(code)
    print(amount)
    df = pd.read_excel("products.xlsx")

    print(df)

    # Directly assigning values to a new row
    df.loc[len(df)] = [name, price, desc,code,amount]
    print(df)

    df.to_excel('products.xlsx', index=False, sheet_name='Product')
    messagebox.showinfo("Success", "Product Added Successfully")
    add_window.destroy()


def add_btn_pressed():
    print("Add Button Pressed")

    add_window = Tk()

    add_window.title("Add Product")

    add_window.geometry("550x650+450+50")

    add_window.config(bg="#0373fc")

    add_product_name_label = Label(add_window, text="Product Name", fg="white", bg="#33914f", font=mini_font)
    add_product_name_label.place(x=20, y=50)

    add_product_price_label = Label(add_window, text="Product Price", fg="white", bg="#33914f", font=mini_font)
    add_product_price_label.place(x=20, y=150)

    add_product_desc_label = Label(add_window, text="Product Desc.", fg="white", bg="#33914f", font=mini_font)
    add_product_desc_label.place(x=20, y=250)

    add_product_code_label = Label(add_window, text="Product code", fg="white", bg="#33914f", font=mini_font)
    add_product_code_label.place(x=20, y=350)

    add_product_amount_label = Label(add_window, text="Product amount", fg="white", bg="#33914f", font=mini_font)
    add_product_amount_label.place(x=20, y=450)


    add_product_name_text = Text(add_window, fg="black", bg="white", font=mini_font)
    add_product_name_text.place(x=225, y=45, width=180, height=50)

    add_product_price_text = Text(add_window, fg="black", bg="white", font=mini_font)
    add_product_price_text.place(x=225, y=145, width=180, height=50)

    add_product_desc_text = Text(add_window, fg="black", bg="white", font=mini_font)
    add_product_desc_text.place(x=225, y=245, width=180, height=50)

    add_product_code_text = Text(add_window, fg="black", bg="white", font=mini_font)
    add_product_code_text.place(x=225, y=345, width=180, height=50)

    add_product_amount_text = Text(add_window, fg="black", bg="white", font=mini_font)
    add_product_amount_text.place(x=225, y=445, width=180, height=50)

    add_product_btn = Button(add_window, text="ADD", fg="white", bg="#33914f", font=mini_font,
                             command=lambda: add_product(add_product_name_text, add_product_price_text,
                                                         add_product_desc_text, add_product_code_text,
                                                         add_product_amount_text,add_window))
    add_product_btn.place(x=150, y=530)

    add_window.mainloop()



def delete_product_function(product_name, view_window):
    df = pd.read_excel('products.xlsx')

    # Delete the row from the dataframe
    df = df[df['Name'] != product_name]

    # Update the Excel file with the modified dataframe
    df.to_excel('products.xlsx', index=False)

    # Optionally, you can provide feedback to the user
    messagebox.showinfo("Success", f"Product with Name: {product_name} deleted successfully.")


    view_window.destroy()


def view_btn_pressed():
    view_window = Tk()
    view_window.geometry("1420x990+100+0")
    view_window.configure(bg="#362657")
    view_window.title("view window")

    df = pd.read_excel('products.xlsx')

    print(df)

    delete_label = Label(view_window, text="Item to Delete", font=mini_font)
    delete_label.place(x=150, y=25)
    delete_text = Text(view_window, bg="white", font=my_font)
    delete_text.place(x=330, y=20, width=220, height=50)
    delete_product_btn = Button(view_window, text="Delete", font=12, bg='red',
                                command=lambda: delete_product_function(delete_text.get("1.0", "end-1c"),
                                                                        view_window))
    delete_product_btn.place(x=600, y=20)

    for index, row in df.iterrows():
         # product_number_label = Label(view_window, text=str(index), font=mini_font)
        # product_number_label.place(x=0, y=100 + 50 * index)

        product_name_label = Label(view_window, text="Name: " + row['Name'], font=mini_font)
        product_name_label.place(x=50, y=100 + 50 * index)

        product_price_label = Label(view_window, text="Price: " + str(row['Price']), font=mini_font)
        product_price_label.place(x=380, y=100 + 50 * index)

        product_desc_label = Label(view_window, text="Desc.: " + str(row['Description']), font=mini_font)
        product_desc_label.place(x=610, y=100 + 50 * index)

        product_code_label = Label(view_window, text="code: " + str(row['code']), font=mini_font)
        product_code_label.place(x=950, y=100 + 50 * index)

        product_amount_label = Label(view_window, text="amount: " + str(row['amount']), font=mini_font)
        product_amount_label.place(x=1260, y=100 + 50 * index)

        product_buy_label=Label(view_window,text="Buy",font=mini_font,bg="#0000ff",fg="white",padx=5,pady=5)
        product_buy_label.place(x=800,y=20)

        product_buy_text=Text(view_window,font=mini_font,bg="white",fg="black")
        product_buy_text.place(x=885,y=20,width=250,height=50)


        product_buy_ok_btn=Button(view_window,text="Ok",font=mini_font,bg="#0dd44f",fg="black",command=lambda :ok_btn_pressed())
        product_buy_ok_btn.place(x=1150,y=20)

        def ok_btn_pressed ():
            messagebox.showinfo("ok,buy","Product bought successfully.")


    view_window.mainloop()


window = Tk()

window.title("Store App")

window.geometry("400x550+450+50")

window.config(bg="#33914f")

my_font = ("arial", 28, "bold")
mini_font = ("arial", 18, "bold")

store_title = Label(window, text="My Store", fg="white", bg="#33914f", font=my_font)
store_title.place(x=120, y=20)

add_image = PhotoImage(file=r"images\add-product.png")
add_image = add_image.subsample(4)
add_button = Button(window, text="Add", fg="black", compound=TOP, image=add_image, font=my_font,
                    command=lambda: add_btn_pressed())
add_button.place(x=50, y=150)

view_image = PhotoImage(file=r"images\view.png")
view_image = view_image.subsample(2)
view_button = Button(window, text="View", fg="black", compound=TOP, image=view_image, font=my_font,
                     command=lambda: view_btn_pressed())
view_button.place(x=220, y=165)

sales_button=Button(text="offers", fg="black",  font=my_font, command=lambda: sales_btn_pressed())
sales_button.place(x=110,y=470)


window.mainloop()

#                                                                                               #teleisio
#                                                                                               #tablet
#                                                                                               #t shirt
#                                                                                               #shoes
##                                                                                              watwr botel
#                                                                                               #note book
#                                                                                               #cie-cre
##                                                                                              orange juic
#                                                                                               #chips
#                                                                                               #glasses
#                                                                                               #connect 4 game
#                                                                                               #cola
#                                                                                               #book