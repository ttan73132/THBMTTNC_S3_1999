class PlayFairCipher:
    def __init__(self) -> None:
        pass

    def create_playfair_matrix(self, key):
        key = key.upper().replace("J", "I")  # Chuyển J thành I trong khóa
        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
        matrix = []
        
        # Thêm ký tự từ key vào matrix, loại bỏ trùng lặp
        for char in key:
            if char not in matrix and char in alphabet:
                matrix.append(char)
        
        # Thêm các ký tự còn lại của alphabet
        for char in alphabet:
            if char not in matrix:
                matrix.append(char)
                
            if len(matrix) == 25:
                break

        playfair_matrix = [matrix[i:i+5] for i in range(0, len(matrix), 5)]
        return playfair_matrix

    def find_letter_coords(self, matrix, letter):
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if matrix[row][col] == letter:
                    return row, col

    def playfair_encrypt(self, plain_text, matrix):
        plain_text = plain_text.replace("J", "I").upper()
        encrypted_text = ""

        # Xử lý văn bản: chèn X vào giữa cặp trùng nhau và xử lý độ dài lẻ
        i = 0
        while i < len(plain_text):
            char1 = plain_text[i]
            char2 = ''
            
            if i + 1 < len(plain_text):
                char2 = plain_text[i+1]
            
            if char1 == char2:
                plain_text = plain_text[:i+1] + 'X' + plain_text[i+1:]
                char2 = 'X'
            elif len(char2) == 0: # Ký tự cuối cùng lẻ
                char2 = 'X'
                
            pair = char1 + char2
            i += 2 # Di chuyển qua cặp vừa xử lý

            row1, col1 = self.find_letter_coords(matrix, pair[0])
            row2, col2 = self.find_letter_coords(matrix, pair[1])

            if row1 == row2:  # Cùng hàng
                encrypted_text += matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
            elif col1 == col2:  # Cùng cột
                encrypted_text += matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
            else:  # Tạo hình chữ nhật
                encrypted_text += matrix[row1][col2] + matrix[row2][col1]

        return encrypted_text

    def playfair_decrypt(self, cipher_text, matrix):
        cipher_text = cipher_text.upper()
        decrypted_text = ""

        for i in range(0, len(cipher_text), 2):
            pair = cipher_text[i:i+2]

            row1, col1 = self.find_letter_coords(matrix, pair[0])
            row2, col2 = self.find_letter_coords(matrix, pair[1])

            if row1 == row2:  # Cùng hàng
                decrypted_text += matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
            elif col1 == col2:  # Cùng cột
                decrypted_text += matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
            else:  # Tạo hình chữ nhật
                decrypted_text += matrix[row1][col2] + matrix[row2][col1]

        return decrypted_text