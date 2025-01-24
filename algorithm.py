def binary_search(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_value = arr[mid]

        if mid_value == target:
            return mid  # پیدا شد!
        elif mid_value < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1  # دیتای مورد نظر پیدا نشد.
def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
        print(f"مرحله {i + 1}: {arr}")

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        print(f"مرحله {i + 1}: {arr}")

def is_operator(char):
    return char in {'+', '-', '*', '/'}

def get_precedence(operator):
    if operator == '+' or operator == '-':
        return 1
    elif operator == '*' or operator == '/':
        return 2
    return 0

def shunting_yard(infix_expression):
    output = []
    operator_stack = []

    for char in infix_expression:
        if char.isalnum():
            output.append(char)
        elif is_operator(char):
            while operator_stack and is_operator(operator_stack[-1]) and get_precedence(operator_stack[-1]) >= get_precedence(char):
                output.append(operator_stack.pop())
            operator_stack.append(char)
        elif char == '(':
            operator_stack.append(char)
        elif char == ')':
            while operator_stack and operator_stack[-1] != '(':
                output.append(operator_stack.pop())
            if operator_stack and operator_stack[-1] == '(':
                operator_stack.pop()

    while operator_stack:
        output.append(operator_stack.pop())

    return output

def infix_to_prefix(infix_expression):
    reversed_output = shunting_yard(reversed(infix_expression))
    prefix_expression = ''.join(reversed(reversed_output))
    return prefix_expression

def infix_to_postfix(infix_expression):
    postfix_expression = ''.join(shunting_yard(infix_expression))
    return postfix_expression


import heapq

def build_heap(arr, heap_type='min'):
    """
    ساخت هیپ از یک آرایه

    پارامترها:
    - arr: آرایه ورودی
    - heap_type: نوع هیپ ('min' برای هیپ کمینه و 'max' برای هیپ بیشینه)
    """
    if heap_type == 'min':
        heapq.heapify(arr)
    elif heap_type == 'max':
        arr = [-element for element in arr]
        heapq.heapify(arr)
        arr = [-element for element in arr]
    else:
        raise ValueError("نوع هیپ نامعتبر! لطفاً 'min' یا 'max' را وارد کنید.")

    return arr

import networkx as nx
import matplotlib.pyplot as plt

def create_graph_from_adjacency_matrix(adjacency_matrix):
    """
    ساخت گراف از یک ماتریس مجاورت

    پارامترها:
    - adjacency_matrix: ماتریس مجاورت گراف
    """
    G = nx.Graph()

    # افزودن یال‌ها به گراف بر اساس ماتریس مجاورت
    for i in range(len(adjacency_matrix)):
        for j in range(i + 1, len(adjacency_matrix[i])):
            if adjacency_matrix[i][j] == 1:
                G.add_edge(i, j)

    return G

def bfs(graph, start_node):
    """
    اجرای الگوریتم BFS بر روی گراف

    پارامترها:
    - graph: گراف
    - start_node: رأس شروع
    """
    visited = set()
    queue = [start_node]

    while queue:
        current_node = queue.pop(0)
        if current_node not in visited:
            print(f"گره {current_node} را بازدید کرد.")
            visited.add(current_node)
            neighbors = list(graph.neighbors(current_node))
            queue.extend(neighbors)


def main_menu():
    while True:
        print("1. جستجوی دودویی")
        print("2. مرتب‌سازی با الگوریتم Selection")
        print("3. مرتب‌سازی با الگوریتم Bubble")
        print("4. تبدیل به عبارت پیشوندی و پسوندی")

        print("5. ساخت هیپ")
        print("6. اجرای کد گراف")
        print("7. اجرای الگوریتم BFS")
        print("8. خروج")

        choice = input("لطفاً شماره گزینه مورد نظر را وارد کنید: ")

        if choice == '1':
            binary_search_menu()
        elif choice == '2':
            arr = list(map(int, input("لطفاً آرایه اعداد (اعداد جدا شده با فاصله) را وارد کنید: ").split()))
            print("آرایه قبل از مرتب سازی:", arr)
            selection_sort(arr)
            print("آرایه مرتب شده:", arr)
            pass
        elif choice == '3':
            arr = list(map(int, input("لطفاً آرایه اعداد (اعداد جدا شده با فاصله) را وارد کنید: ").split()))
            print("آرایه قبل از مرتب سازی:", arr)
            bubble_sort(arr)
            print("آرایه مرتب شده:", arr)     

        elif choice == '4':
                # تبدیل به عبارت پیشوندی و پسوندی
            infix_expression = input("لطفاً عبارت میانوندی را وارد کنید: ")
            prefix_expression = infix_to_prefix(infix_expression)
            postfix_expression = infix_to_postfix(infix_expression)
            print(f"عبارت پیشوندی: {prefix_expression}")
            print(f"عبارت پسوندی: {postfix_expression}")     
            
        elif choice == '5':
            try:
                # دریافت آرایه از کاربر
                arr = list(map(int, input("لطفاً آرایه اعداد (اعداد جدا شده با فاصله) را وارد کنید: ").split()))

                # انتخاب نوع هیپ (کمینه یا بیشینه)
                heap_type = input("لطفاً نوع هیپ را انتخاب کنید (min/max): ").lower()

                # ساخت هیپ
                heap = build_heap(arr, heap_type)

                # نمایش هیپ حاصل
                print(f"هیپ {heap_type} حاصل:")
                print(heap)

            except ValueError as e:
                print(f"خطا: {e}")

        elif choice == '6':
            try:
                # دریافت ماتریس مجاورت از کاربر
                adjacency_matrix = []
                n = int(input("تعداد رئوس گراف را وارد کنید: "))
                print("لطفاً ماتریس مجاورت گراف را وارد کنید:")
                for _ in range(n):
                    row = list(map(int, input().split()))
                    adjacency_matrix.append(row)

                # ساخت گراف از ماتریس مجاورت
                G = create_graph_from_adjacency_matrix(adjacency_matrix)

                # نمایش گراف
                nx.draw(G, with_labels=True, font_weight='bold', node_color='skyblue', font_color='black')
                plt.show()
            except ValueError:
                print("ورودی نامعتبر! لطفاً اطمینان حاصل کنید که اعداد وارد شده از نوع صحیح هستند.")
        
        elif choice == '7':
            try:
                # اجرای الگوریتم BFS
                start_node = int(input("رأس شروع الگوریتم BFS را وارد کنید: "))
                bfs(G, start_node)
            except NameError:
                print("ابتدا گراف را ایجاد کنید.")
            except ValueError:
                print("ورودی نامعتبر! لطفاً اطمینان حاصل کنید که شماره رأس از نوع صحیح است.")

        elif choice == '8':
            print("خروج از برنامه.")
            break
        else:
            print("گزینه نامعتبر. لطفاً یک شماره معتبر را وارد کنید.")

def binary_search_menu():
    try:
        # دریافت آرایه و دیتای مورد نظر از کاربر
        arr = list(map(int, input("لطفاً آرایه مرتب (اعداد جدا شده با فاصله) را وارد کنید: ").split()))
        target = int(input("لطفاً دیتای مورد نظر را وارد کنید: "))

        # جستجوی دودویی
        result = binary_search(arr, target)

        # نمایش نتیجه
        if result != -1:
            print(f"دیتای مورد نظر در ایندکس {result} یافت شد.")
        else:
            print("دیتای مورد نظر یافت نشد.")
    except ValueError:
        print("ورودی نامعتبر! لطفاً اطمینان حاصل کنید که آرایه اعداد صحیح مرتب و دیتای مورد نظر نیز یک عدد صحیح باشد.")

if __name__ == "__main__":
    main_menu()
