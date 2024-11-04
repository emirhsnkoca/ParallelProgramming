def calculate_pyramid_height(number_of_blocks):
    
    height = 0
    while number_of_blocks >= (height + 1):
                                                     # Her kat için gereken blok sayısını kontrol ediyoruz.
        height += 1                                  # Her katta yüksekliği çıkartıyoruz. 1.katta 1 , 2de 2 ,3 te 3 böylelikle tüm katlar yüksekliğine göre blokltan oluşuyor.
        number_of_blocks -= height                     
    
    return height  

