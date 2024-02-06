from PIL import Image

image_path = "image.png"
original_image = Image.open(image_path)

square_size = 351
row_sep = 62
col_sep = 132

row_letters = "akstnhmyrwngzdbp"
col_letters = "aiueo"

for row_idx, row_letter in enumerate(row_letters):
    for col_idx, col_letter in enumerate(col_letters):
        left = col_idx * (square_size + col_sep)
        upper = row_idx * (square_size + row_sep)
        right = left + square_size
        lower = upper + square_size
        
        square = original_image.crop((left, upper, right, lower))
        square_path = f"new/square_{row_letter}_{col_letter}.png"
        square.save(square_path)

original_image.close()
