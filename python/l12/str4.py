const1 = "CONSTANT_VALUE IS 3.14"
const1 = const1.lower()
print(const1)
if (const1.isupper()) :
    print("Correct")
else:
    print("Not correct")


const2 = "const-var-for-gravitational-force"
#CONST_VAR_FOR
const2_correct = const2.replace('-', '_').upper()
print(const2_correct)
if (const2_correct.isupper()) :
    print("Correct")
else:
    print("Not correct")


book_title = "A moVeaBlE fEasT"
print(book_title.title())
print(book_title.capitalize())


