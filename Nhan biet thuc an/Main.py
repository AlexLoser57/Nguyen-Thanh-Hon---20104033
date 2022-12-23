import tkinter as tk
from PIL import ImageTk, Image
from tkinter import filedialog
import numpy as np
import tensorflow as tf
import re
from tkinter import messagebox
from youtube_search import YoutubeSearch
import webbrowser
from tensorflow import keras
from tensorflow.keras.utils import load_img, img_to_array
from googletrans import Translator
new_model = tf.keras.models.load_model("FoodRec3.h5")


def load_img():
    global img, image_data
    for img_display in frame.winfo_children():
        img_display.destroy()

    image_data = filedialog.askopenfilename(initialdir="/", title="Choose an image",
                                            filetypes=(("all files", "*.*"), ("png files", "*.png")))
    basewidth = 250
    img = Image.open(image_data)
    wpercent = (basewidth / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    img = img.resize((basewidth, hsize), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    panel_image = tk.Label(frame, image=img).pack()


def classify():
    original = Image.open(image_data)
    original = original.resize((150, 150), Image.ANTIALIAS)
    numpy_image = img_to_array(original)
    image_batch = np.expand_dims(numpy_image, axis=0)
    #processed_image = new_model.preprocess_input(image_batch.copy())
    result = new_model.predict(image_batch)
    global prediction
    if round(result[0][0]) == 1:
        prediction = 'Bánh bèo'
    if round(result[0][1]) == 1:
        prediction = 'Bánh bột lọc'
    if round(result[0][2]) == 1:
        prediction = 'Bánh căn'
    if round(result[0][3]) == 1:
        prediction = 'Banh canh'
    if round(result[0][4]) == 1:
        prediction = 'Bánh chưng'
    if round(result[0][5]) == 1:
        prediction = 'Bánh cuốn'
    if round(result[0][6]) == 1:
        prediction = 'Bánh đúc'
    if round(result[0][7]) == 1:
        prediction = 'Bánh giò'
    if round(result[0][8]) == 1:
        prediction = 'Bánh khọt'
    if round(result[0][9]) == 1:
        prediction = 'Bánh mì'
    if round(result[0][10]) == 1:
        prediction = 'Bánh pía'
    if round(result[0][11]) == 1:
        prediction = 'Bánh tét'
    if round(result[0][12]) == 1:
        prediction = 'Bánh tráng nướng'
    if round(result[0][13]) == 1:
        prediction = 'Bánh xèo'
    if round(result[0][14]) == 1:
        prediction = 'Bún bò huế'
    if round(result[0][15]) == 1:
        prediction = 'Bún đậu mắm tôm'
    if round(result[0][16]) == 1:
        prediction = 'Bún mắm'
    if round(result[0][17]) == 1:
        prediction = 'Bún riêu'
    if round(result[0][18]) == 1:
        prediction = 'Bún thịt nướng'
    if round(result[0][19]) == 1:
        prediction = 'Cá kho tộ'
    if round(result[0][20]) == 1:
        prediction = 'Canh chua'
    if round(result[0][21]) == 1:
        prediction = 'Cao lầu'
    if round(result[0][22]) == 1:
        prediction = 'Cháo lòng'
    if round(result[0][23]) == 1:
        prediction = 'Cơm tấm'
    if round(result[0][24]) == 1:
        prediction = 'Gỏi cuốn'
    if round(result[0][25]) == 1:
        prediction = 'Hủ tiếu'
    if round(result[0][26]) == 1:
        prediction = 'Mì Quảng'
    if round(result[0][27]) == 1:
        prediction = 'Nem chua'
    if round(result[0][28]) == 1:
        prediction = 'Phở'
    if round(result[0][29]) == 1:
        prediction = 'Xôi xéo'
    print("Đây là :", str(prediction).upper())

    d = {"Bún bò huế": "Là một trong những đặc sản của xứ Huế. Tại Huế, món này được gọi đơn giản là 'bún bò'.\nHương vị: vị cay nồng, mùi sả đặc trưng của nước lèo.",
         'Bánh xèo': "Bánh Xèo rất hấp dẫn thực khách bởi cách ăn của nó đúng điệu phải dùng tay để gói. Trải những chiếc lá non lên bàn tay, bỏ vào một chút bánh kèm nhân, cuộn lại chấm nước mắm chanh, tỏi, ớt… từ từ nhai mà tận hưởng cái mùi vị của cây trái vườn nhà.",
         "Xôi xéo": "Xôi xéo được nấu từ loại nếp dẻo thơm và đậu xanh chắc hạt. Để có được gói xôi xéo thơm ngon, đòi hỏi người nấu phải cần thận, tỉ mỉ. Xôi xéo ăn kèm dừa bào sợi, đậu phộng hay mè rang, rưới thêm chút nước mỡ gà, hành phi vàng ngon khó cưỡng. ",
         "Nem chua": "Thưởng thức món nem của xứ Thanh, bạn sẽ phải say đắm với vị giòn, ngon của bì lợn, vị chua của thịt, vị cay của ớt, tỏi… Bên cạnh đó, người dân còn khéo léo cho thêm vị nồng của lá đinh lăng tạo nên một hương vị ẩm thực ngon khó tả. ",
         "Mì Quảng": "Mì Quảng là một trong những món ngon đặc sản miền Trung vừa bình dị, vừa dân dã. Sợi mì Quảng cũng được làm từ bột gạo như các loại bún, phở,... nhưng lại có sắc thái và hương vị hoàn toàn khác.",
         'Hủ tiếu': "Nếu phở là lựa chọn của nhiều người khi đến Hà Nội thì hủ tiếu là món ăn bạn phải thử trong chuyến khám phá ẩm thực Sài thành. Với sự biến tấu độc lạ, hủ tiếu có nhiều phiên bản thu hút thực khách.",
         'Gỏi cuốn': "Gỏi cuốn là món cuốn với hương vị thơm ngon, thanh mát và dễ thực hiện luôn xuất hiện trong những bữa ăn, bữa tiệc của gia đình người Việt.",
         'Bún đậu mắm tôm': "Bún đậu mắm tôm được xem như một trong những món ăn truyền thống của người Hà Nội xưa. Sự kết hợp giữa bún, đậu chiên giòn, rau, thịt luộc và một bát mắm tôm chua cay đậm vị sạch sẽ sẽ làm nên món ăn với hương vị khó quên nhất và lại đảm bảo sức khỏe!",
         'Bánh bột lọc': 'Bánh bột lọc, một trong những loại bánh đặc trưng của miền đất cố đô Huế. Thành phần chính của nhân bánh bột lọc thường là tôm thịt. ',
         'Bánh căn': 'Bánh căn là một loại bánh phổ biến của Ninh Thuận, Bình Thuận. Bánh căn thường ít được dọn cùng rau sống ăn lá, mà thường ăn kèm với xoài xanh, khế chua, dưa leo băm sợi.',
         'Bánh chưng': 'Bánh chưng được phối hợp tổng hòa nhiều mùi vị như thơm dẻo của gạo nếp, ngọt bùi của đậu xanh, vị béo ngậy của thịt mỡ và mùi thơm đặc trưng của tiêu, hành, lá dong. Đây là sự kết hợp tương đồng rất khoa học và sáng tạo phù hợp nhu cầu dinh dưỡng nhiều lứa tuổi.',
         'Bánh cuốn': 'Bánh cuốn là món ăn đặc trưng của ẩm thực Việt Nam, với lớp vỏ bánh được tráng mỏng, mềm, dẻo dai được cuộn nhiều loại nhân khác nhau bên trong.Bánh cuốn thường được ăn kèm với các loại chả lụa, chả quế, nem chua, dưa leo và giá đỗ, chấm cùng nước mắm ngọt hoặc dùng kèm nước dùng ninh từ xương.',
         'Bánh đúc': 'Là món ăn dân dã thịnh hành khắp ba miền, bánh đúc ăn giòn, mát, mịn, no bụng mà lại dễ tiêu, dễ làm và giá thành cũng rất rẻ. Không chỉ được ăn như một thức quà quê, bữa ăn sáng mà điển hình là bánh đúc chấm tương, bánh đúc cũng có thể ăn kèm với canh riêu cua, rau thơm, mắm tôm, mật ong, mật mía, mứt trái cây và thậm chí cả cá kho, thịt kho tùy thích',
         'Bánh giò': 'Bánh giò là một loại bánh được làm bằng bột gạo tẻ, bột năng hòa với nước xương hầm, nhân làm từ thịt nạc vai có kèm mộc nhĩ, hành tím khô, hành ta, hạt tiêu, nước mắm, muối, (ở Miền Nam nhân bánh còn có thêm trứng cút)',
         'Bánh khọt': 'Bánh khọt là loại bánh Việt Nam (chính xác là loại bánh đặc trưng của miền nam Việt Nam) làm từ bột gạo hoặc bột sắn, có nhân tôm, được nướng và ăn kèm với rau sống, ớt tươi, thường ăn với nước mắm pha ngọt, rất ít khi chấm nước sốt mắm tôm (không phải mắm tôm hay mắm tôm chua).',
         'Bánh mì': 'Bánh mì được xem như một loại thức ăn nhanh bình dân và thường được tiêu thụ trong bữa sáng hoặc bất kỳ bữa phụ nào trong ngày. Do có giá thành phù hợp nên bánh mì trở thành món ăn được rất nhiều người ưa chuộng.',
         'Bánh pía': 'Tại Việt Nam, bánh pía là một trong những đặc sản của Sóc Trăng, do người Hoa di cư vào miền Nam sáng tạo ra. Bánh pía được làm từ bột mì nhào mỡ nước từ heo.',
         'Bánh tét': 'Nguyên liệu để gói bánh tét ngày Tết tương tự như dùng làm bánh chưng, bao gồm: gạo nếp, đậu xanh tách vỏ, thịt heo và một số gia vị tương tự như để làm bánh chưng. Nhưng phổ biến và bán quanh năm là bánh tét ngọt (nhân chuối, thường là chuối Xiêm) hay bánh tét chay (nhân đậu đen)',
         'Bánh tráng nướng': 'Bánh tráng nướng – đặc sản Đà Lạt nay đã len lỏi vào nhịp sống của người dân ở khắp mọi miền. Bởi rất dễ ăn và mùi vị đặc trưng rất thơm ngon',
         'Phở': 'Phở xứng đáng là “linh hồn” ẩm thực Việt, đưa tên Việt Nam định vị rõ nét trên bản đồ ẩm thực thế giới. Khi thưởng thức, bạn hãy ăn chậm để cảm nhận. Thịt mềm, bánh phở dẻo, nước dùng đậm đà pha chút vị chua thanh thanh của chanh tươi, chút cay dịu của gừng, cay nồng từ ớt, thơm nồng từ hành lá,… Tất cả hoà quyện tạo nên hương vị thơm ngon độc đáo của món phở, kích thích vị giác của người thưởng thức.',
         'Cơm tấm': 'Khi thưởng thức cơm tấm Sài Gòn, bạn sẽ cảm nhận được hạt cơm tấm dẻo thơm, vị chả trứng béo ngậy, sườn bì bùi thơm và không thể thiết vài lát dưa chuột giòn ngon, cà chua sống thái lát thanh mát. Tất cả hòa quyện tạo nên hương vị đậm đà đặc trưng khó lẫn với bất kỳ món cơm nào khác.',
         'Cháo lòng': 'Cháo lòng là một trong những món được yêu thích bởi nhiều thực khách tại Việt Nam. Không những có mùi vị thơm nồng, ngon mà còn vô cùng bổ dưỡng, thích thích tiêu hóa.',
         'Cao lầu': 'Có thể nói thưởng thức Cao Lầu giúp thực khách đánh thức mọi giác quan từ tiếng sựt sựt của sợi mì, hương thơm của mắm, nước tương, mùi ngầy ngậy của tép mỡ hòa cùng vị thơm ngọt của tôm, thịt xá xíu, quyện cùng đủ mùi vị cay nồng, đắng, chát của rau ghém.',
         'Canh chua': 'Canh chua là món ăn được người Việt vô cùng yêu thích nhờ nhiều tầng hương vị thơm ngon, tươi mát. Bát canh chua ngọt dịu nhẹ cực đưa cơm, dù là thưởng thức vào ngày hè hay mùa đông cũng đều phù hợp.',
         'Cá kho tộ': 'Nói đến miền đất phương Nam ta nghĩ ngay đến hệ thống kênh rạch, sông suối chằng chịt khắp vùng cung cấp rất nhiều thủy sản đa dạng. Có lẽ bắt nguồn từ sự phong phú của các loại thủy sản thiên nhiên này mà văn hóa ẩm thực của nơi đây rất đa dạng, nhiều cách chế biến nấu nướng độc đáo và đậm đà. Cá kho tộ – Món ăn đậm đà, thơm ngon cũng có nguồn gốc từ miền đất thú vị này. Cá kho tộ có hương vị cá ngọt mềm, thơm ngậy, chút mằn mặn của nước mắm se se vị cay của ớt đã tạo nên hương vị đặc trưng của món ăn này.',
         'Bún thịt nướng': 'Bún thịt nướng là món ăn mang đậm hương vị Việt Nam. Với sợi bún mềm, thịt nướng vàng giòn cùng nước mắm chua ngọt khiến thực khách thích mê.Bún thịt nướng sẽ ngon hơn nếu bạn sử dụng thịt ba chỉ, có chút mỡ xen kẽ ăn sẽ không bị khô. Nhưng đừng nên chọn miếng thịt có quá nhiều mỡ, ăn sẽ bị ngấy.',
         'Bún riêu': 'Trong các món ăn miền Bắc, bún riêu cua là món ăn ngon có vị riêng từ cua, thơm mùi mắm tôm, cùng nước dùng chua ngọt thanh thanh rất thích hợp với những ngày hè nóng nực.',
         'Bún mắm': 'Bún mắm từ lâu đã trở thành món ăn quen thuộc của người dân Nam Bộ nói chung và đặc biệt là người dân Miền Tây nói riêng. Nó được xem là ẩm thực đặc trưng của vùng đất miền Tây - Chưa ăn bún mắm chưa phải người Miền Tây.'}

    table = tk.Label(frame, text=str("Món này là : ").upper()).pack()
    realgang2 = tk.Label(frame, text=str(prediction).upper(),
                         bg='white', font=("", 30)).pack()
    realgang = tk.Message(frame, width=350, justify='left',
                          text=str(d[prediction]), font=("times", 16)).pack()


def inforfood():
    T = messagebox.askyesno('Thông báo',
                            'Bạn có muốn tìm hiểu cách nấu món ăn trên youtube ?')
    if T == True:
        result = YoutubeSearch(prediction, max_results=10).to_dict()
        url = 'http://youtube.com' + result[0]['url_suffix']
        webbrowser.open(url)
        T1 = messagebox.askokcancel(
            'Thông báo', 'Trang web bạn yêu cầu đã được mở !')


wd = tk.Tk()
ico = Image.open('Logo.png')
icon = ImageTk.PhotoImage(ico)
wd.wm_iconphoto(False, icon)

wd.title('NHẬN DIỆN ĐỒ ĂN VIỆT NAM')
wd.resizable(False, False)

canvas = tk.Canvas(wd, height=800, width=450, bg='grey')
canvas.pack()
frame = tk.Frame(wd, width=450, height=900, bg='white')
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

chose_image = tk.Button(wd, text='Chọn ảnh', padx=10,
                        pady=10, fg="white", bg="lightcoral", command=load_img)
moreinfor = tk.Button(wd, text='Tìm hiểu thêm về món ăn',
                      padx=10, pady=10, fg="white", bg="green", command=inforfood)
class_image = tk.Button(wd, text='Nhận diện ảnh', padx=10,
                        pady=10, fg="white", bg="dodger blue", command=classify)

moreinfor.pack(side=tk.RIGHT)
chose_image.pack(side=tk.LEFT)
class_image.pack(side=tk.RIGHT)

wd.mainloop()
