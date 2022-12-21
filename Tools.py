# Create by ruiyang in 2022/12/16 ~ Version: Python 3.10
from tkinter import *
from pyperclip import *
from tkinter import messagebox
from tkinter import ttk
import logging
import re


class Home:
    def __init__(self):
        # 父容器
        self.root = Tk()
        # window.geometry("宽度x高度+屏幕X坐标+屏幕Y坐标")
        self.root.geometry("400x220+640+360")
        self.root.title("Tools")
        # 设置图标，此处的False表示此图标图像仅适用于此特定窗口，但不适用于未来创建的顶层。
        self.root.iconphoto(False, PhotoImage(file='Pinkpig.PNG'))
        # 可变变量
        self.user_input = StringVar()
        self.user_input_part = None
        logging.basicConfig(level=logging.INFO, format=' %(asctime)s - %(levelname)s - %(message)s')
        logging.info('__init__ - succeed in setting variables')

    def home(self):
        self.destroy_all()
        self.menu()
        Label(self.root, font='monaco', text='\n\n\n\n欢迎使用Tools，左上角选择功能').pack()
        logging.info('main_window - succeed in creating widgets')

    def menu(self):
        # 父类菜单栏模版
        # 菜单父容器，参数写窗口
        main_menu = Menu(self.root)
        # 菜单子容器
        menu_contents = Menu(main_menu)
        # 菜单项
        main_menu.add_cascade(label="目录", menu=menu_contents)
        self.root.config(menu=main_menu)

    # 关于窗口
    def about_window(self):
        self.destroy_all()
        self.menu()
        Label(self.root, text='\n\n\n\n编码unicode都采用UTF-8字符编码\n更多功能持续开发中😽\n', relief=FLAT).pack()
        Button(self.root, text='复制github地址', command=self.copy_github, cursor='star', relief=RAISED).pack()
        Label(self.root, text='Author: @Rui-yang', font='monaco', relief=FLAT).pack(side=BOTTOM)
        logging.info('about - succeed in creating widgets')

    @staticmethod
    # 复制github地址
    def copy_github():
        copy('https://github.com/SmartSunruiyang/Pink_pig-Tools.git')
        messagebox.showinfo('复制成功！', '已复制github地址到剪切板')
        logging.info('copy - succeed in copying github address')

    # 删除窗口所有控件
    def destroy_all(self):
        # 父类清空控件方法
        self.user_input.set('')
        # winfo_children() 返回一个列表，列表中包含窗口中所有的控件
        __list = self.root.winfo_children()
        for item in __list:
            item.destroy()

    def main(self):
        self.root.mainloop()


# 完成ascii码转换的类
class EncodeConversation(Home):
    def __init__(self):
        super(EncodeConversation, self).__init__()

    def menu(self):
        # 菜单父容器，参数写窗口
        main_menu = Menu(self.root)
        # 菜单子容器
        menu_contents = Menu(main_menu)
        # 菜单项
        main_menu.add_cascade(label="目录", menu=menu_contents)
        menu_contents.add_command(label="编码转换工具", command=self.encode_window)
        self.root.config(menu=main_menu)

    def encode_window(self):
        self.__main_window()

    # 主要部件
    def __main_window(self):
        self.destroy_all()
        self.__menu_encode()
        Label(self.root, font='monaco', text='\n\n输入您想要转换为ASCII码的字符').pack()
        self.user_input_part = Entry(self.root, textvariable=self.user_input)
        self.user_input_part.pack()
        Button(self.root, text='转换', command=self.__change).pack()
        Button(self.root, text='复制', command=self.__copy).pack()
        # 清空输入框的按钮
        Button(self.root, text='清空', command=self.__clear).pack()
        logging.info('main_window - ascii - succeed in creating widgets')

    def __menu_encode(self):
        # 菜单父容器，参数写窗口
        main_menu = Menu(self.root)
        # 菜单子容器
        menu_contents = Menu(main_menu)
        # 菜单项
        main_menu.add_cascade(label="目录", menu=menu_contents)
        menu_contents.add_command(label="字符转换ASCII", command=self.encode_window)
        menu_contents.add_command(label="ASCII转换字符", command=self.__reverse_window)
        menu_contents.add_command(label="ASCII转unicode", command=self.__unicode_window)
        menu_contents.add_command(label="unicode转ASCII", command=self.__unicode_reverse_window)
        menu_contents.add_command(label="unicode转字符", command=self.home)
        menu_contents.add_command(label="字符转unicode", command=self.home)
        menu_contents.add_command(label="主页", command=self.home)
        self.root.config(menu=main_menu)

    # 逆向转换的窗口
    def __reverse_window(self):
        self.destroy_all()
        self.__menu_encode()
        Label(self.root, font='monaco', text='\n\n输入您想要转换为字符的ASCII码 (分号隔开)').pack()
        self.user_input_part = Entry(self.root, textvariable=self.user_input)
        self.user_input_part.pack()
        Button(self.root, text='转换', command=self.__change_reverse).pack()
        Button(self.root, text='复制', command=self.__copy).pack()
        # 清空输入框的按钮
        Button(self.root, text='清空', command=self.__clear).pack()
        logging.info('main_window - ascii - reverse - succeed in creating widgets')

    # 改变输入框中的值为ASCII
    def __change(self):
        data_string = ''
        data_list = list(str(self.user_input.get()))
        # 格式化输出
        for data in data_list:
            data_string += f'&#{str(ord(data))};'
        self.user_input.set(data_string)
        logging.info('change - succeed in changing self.user_input -> StringVar()')
        return self.user_input

    # 改变输入框的值为字符
    def __change_reverse(self):
        data_string = ''
        ascii_string = self.user_input.get()
        status = True
        # 将用户输入的ASCII分隔成列表
        if ascii_string.startswith('&#'):
            ascii_list = re.split(';', ascii_string)
        else:
            ascii_list = re.split('[;；]', ascii_string)
            status = False
        try:
            # 格式化输出
            for item in ascii_list:
                if item != '':
                    if status:
                        data_string += f'{chr(int(item[2:]))}'
                    else:
                        data_string += f'{chr(int(item))}'
            self.user_input.set(data_string)
            logging.info('change - reverse - succeed in changing self.user_input -> StringVar()')
        except Exception as e:
            logging.error(f'change - ASCII is not exist or {e}')
            messagebox.showerror('错误！', '请输入正确的ASCII码并用-空格，逗号，分号隔开')

    # ASCII转unicode窗口
    def __unicode_window(self):
        self.destroy_all()
        self.__menu_encode()
        Label(self.root, font='monaco', text='\n\n输入您想要转换为unicode UTF-8的ASCII').pack()
        self.user_input_part = Entry(self.root, textvariable=self.user_input)
        self.user_input_part.pack()
        Button(self.root, text='转换', command=self.__change_unicode).pack()
        Button(self.root, text='复制', command=self.__copy).pack()
        # 清空输入框的按钮
        Button(self.root, text='清空', command=self.__clear).pack()
        logging.info('main_window - ascii - unicode - succeed in creating widgets')

    # 改变输入框中的值为unicode
    def __change_unicode(self):
        data_string = ''
        ascii_string = self.user_input.get()
        status = True
        # 将用户输入的ASCII分隔成列表
        if ascii_string.startswith('&#'):
            ascii_list = re.split(';', ascii_string)
        else:
            ascii_list = re.split('[;；]', ascii_string)
            status = False
        try:
            # 格式化输出
            for item in ascii_list:
                if item != '':
                    if status:
                        data_string += f'{chr(int(item[2:]))}'.encode('unicode_escape').decode('utf-8')
                    else:
                        data_string += f'{chr(int(item))}'.encode('unicode_escape').decode('utf-8')
            self.user_input.set(data_string)
            logging.info('change - unicode - succeed in changing self.user_input -> StringVar()')
        except Exception as e:
            logging.error(f'change - unicode - ASCII is not exist or {e}')
            messagebox.showerror('错误！', '请输入正确的ASCII码并用-空格，逗号，分号隔开')

    # unicode转ASCII窗口
    def __unicode_reverse_window(self):
        self.destroy_all()
        self.__menu_encode()
        Label(self.root, font='monaco', text='\n\n输入您想要转换为ASCII的unicode UTF-8').pack()
        self.user_input_part = Entry(self.root, textvariable=self.user_input)
        self.user_input_part.pack()
        Button(self.root, text='转换', command=self.__change_unicode_reverse).pack()
        Button(self.root, text='复制', command=self.__copy).pack()
        # 清空输入框的按钮
        Button(self.root, text='清空', command=self.__clear).pack()
        logging.info('main_window - ascii - unicode - succeed in creating widgets')

    # 改变输入框中的值为ASCII
    def __change_unicode_reverse(self):
        data_string = ''
        data = self.user_input.get()
        # 将字符串六个一组分隔成列表，此正则表达式表示精确匹配6个任意字符
        data_list = re.findall(r'.{6}', data)
        try:
            # 格式化输出
            for data in data_list:
                data_string += f"&#{str(ord(data.encode('utf-8').decode('unicode-escape')))};"
            self.user_input.set(data_string)
            logging.info('change - unicode - reverse - succeed in changing self.user_input -> StringVar()')
        except Exception as e:
            logging.error(f'change - unicode - reverse - unicode is not exist or {e}')
            messagebox.showerror('错误！', '请输入正确的unicode UTF-8码')

    # unicode转字符串窗口
    def __unicode_string_window(self):
        self.destroy_all()
        self.__menu_encode()
        Label(self.root, font='monaco', text='\n\n输入您想要转换为字符串的unicode UTF-8').pack()
        self.user_input_part = Entry(self.root, textvariable=self.user_input)
        self.user_input_part.pack()
        Button(self.root, text='转换', command=self.__change_unicode_string).pack()
        Button(self.root, text='复制', command=self.__copy).pack()
        # 清空输入框的按钮
        Button(self.root, text='清空', command=self.__clear).pack()
        logging.info('main_window - ascii - unicode - succeed in creating widgets')

    # 改变输入框中的值为字符串
    def __change_unicode_string(self):
        data_string = ''
        data = self.user_input.get()
        # 将字符串六个一组分隔成列表，此正则表达式表示精确匹配6个任意字符
        data_list = re.findall(r'.{6}', data)
        try:
            # 格式化输出
            for data in data_list:
                data_string += f"{data.encode('utf-8').decode('unicode-escape')}"
            self.user_input.set(data_string)
            logging.info('change - unicode - string - succeed in changing self.user_input -> StringVar()')
        except Exception as e:
            logging.error(f'change - unicode - string - unicode is not exist or {e}')
            messagebox.showerror('错误！', '请输入正确的unicode UTF-8码')

    # 字符串转unicode窗口
    def __string_unicode_window(self):
        self.destroy_all()
        self.__menu_encode()
        Label(self.root, font='monaco', text='\n\n输入您想要转换为unicode UTF-8的字符串').pack()
        self.user_input_part = Entry(self.root, textvariable=self.user_input)
        self.user_input_part.pack()
        Button(self.root, text='转换', command=self.__change_string_unicode).pack()
        Button(self.root, text='复制', command=self.__copy).pack()
        # 清空输入框的按钮
        Button(self.root, text='清空', command=self.__clear).pack()
        logging.info('main_window - ascii - unicode - succeed in creating widgets')

    # 改变输入框中的值为unicode
    def __change_string_unicode(self):
        data_string = ''
        data_list = list(str(self.user_input.get()))
        try:
            # 格式化输出
            for data in data_list:
                data_string += data.encode('unicode-escape').decode('utf-8')
            self.user_input.set(data_string)
            logging.info('change - string - unicode - succeed in changing self.user_input -> StringVar()')
        except Exception as e:
            logging.error(f'change - string - unicode - string is not exist or {e}')
            messagebox.showerror('错误！', '请输入正确的字符串')

    # 复制ASCII
    def __copy(self):
        copy(self.user_input.get())
        messagebox.showinfo('复制成功！', '已复制到剪贴板')
        logging.info('copy - succeed in copying self.user_input -> StringVar()')

    # 清空输入框
    def __clear(self):
        self.user_input.set('')
        logging.info('clear - succeed in clearing self.user_input -> StringVar()')


# 完成进制转换的类
class BaseConversation(EncodeConversation):
    def __init__(self):
        super(BaseConversation, self).__init__()
        self._choice = StringVar()
        self._choice_2 = StringVar()
        self.show_entry = StringVar()
        self.combobox_object = None
        self.combobox_target = None

    def menu(self):
        # 菜单父容器，参数写窗口
        main_menu = Menu(self.root)
        # 菜单子容器，参数写父容器
        menu_contents = Menu(main_menu)
        # 菜单项
        main_menu.add_cascade(label="目录", menu=menu_contents)
        menu_contents.add_command(label="编码转换工具", command=self.encode_window)
        menu_contents.add_command(label="进制转换工具", command=self.conversation_window)
        menu_contents.add_command(label="关于", command=self.about_window)
        self.root.config(menu=main_menu)

    def conversation_window(self):
        self.__conversation_window()

    # 主要部件
    def __conversation_window(self):
        self.destroy_all()
        self.__menu_conversation()
        command_list = ['二进制', '八进制', '十进制', '十六进制']
        self.combobox_object = ttk.Combobox(self.root, textvariable=self._choice, values=command_list,
                                            state='readonly')
        self.combobox_object.pack()
        Entry(self.root, textvariable=self.user_input).pack()
        Label(self.root, text='转化为', relief=FLAT).pack()
        self.combobox_target = ttk.Combobox(self.root, textvariable=self._choice_2, values=command_list,
                                            state='readonly')
        self.combobox_target.pack()
        Entry(self.root, textvariable=self.show_entry).pack()
        Button(self.root, text='转换', command=self.__change_base).pack()
        Button(self.root, text='复制', command=self.__copy).pack()
        # 清空输入框的按钮
        Button(self.root, text='清空', command=self.__clear).pack()
        logging.info('main_window - bin To dec - succeed in creating widgets')

    def __menu_conversation(self):
        # 菜单父容器，参数写窗口
        main_menu = Menu(self.root)
        # 菜单子容器
        menu_contents = Menu(main_menu)
        # 菜单项
        main_menu.add_cascade(label="目录", menu=menu_contents)
        menu_contents.add_command(label="主页", command=self.home)
        self.root.config(menu=main_menu)

    # 改变输入框中的值
    def __change_base(self):
        try:
            base_object = self.combobox_object.current()
            user_input = self.user_input.get()
            base_target = self.combobox_target.current()
            # 进制字典
            base_dict = {0: 2, 1: 8, 2: 10, 3: 16}
            # 进制转换
            command_dict = {
                0: lambda x: bin(int(x, base_dict[base_object])).replace('0b', ''),
                1: lambda x: oct(int(x, base_dict[base_object])).replace('0o', ''),
                2: lambda x: str(int(x, base_dict[base_object])),
                3: lambda x: hex(int(x, base_dict[base_object])).replace('0x', '')
            }
            self.show_entry.set(command_dict[base_target](user_input))
            logging.info('change - succeed in changing self.show_entry -> StringVar()')
        except ValueError:
            messagebox.showerror('错误！', '请输入对应进制正确的数')
            self.__clear()
            logging.error('change - number is not exist')

    # 复制进制转换后的数
    def __copy(self):
        copy(self.show_entry.get())
        messagebox.showinfo('复制成功！', '已复制进制转换后的数到剪切板')
        logging.info('copy - succeed in copying self.show_entry -> StringVar()')

    # 清空输入框
    def __clear(self):
        self.user_input.set('')
        logging.info('clear - succeed in clearing self.user_input -> StringVar()')
        self.show_entry.set('')
        logging.info('clear - succeed in clearing self.show_entry -> StringVar()')

    def destroy_all(self):
        # 重写清空控件方法
        self.user_input.set('')
        self.show_entry.set('')
        # winfo_children() 返回一个列表，列表中包含窗口中所有的控件
        __list = self.root.winfo_children()
        for item in __list:
            item.destroy()


# 从最子类实例化
if __name__ == '__main__':
    BaseConversation().home()
    mainloop()





