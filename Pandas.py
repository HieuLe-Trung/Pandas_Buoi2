# 1/ Show the first 5 lines of tsv file.
def show_5line():
    with open('04_gap-merged.tsv', 'r') as file:
        for i in range(5):
            line = file.readline().strip()
            print(line)


# 2/ Find the number of row and column of this file.
def numberRow_Col():
    with open('04_gap-merged.tsv', 'r') as file:
        numbRow = 0
        numbCol = 0
        for i in file:
            numbRow += 1
            numbCol = max(numbCol, len(i.strip().split('\t')))

    print("So dòng: ", numbRow)
    print("So cột: ", numbCol)


# 3/ Print the name of the columns.
def printColName():
    with open('04_gap-merged.tsv', 'r') as file:
        name = file.readline().strip().split('\t')
        for colName in name:
            print(colName)


# 4/ What is the type of the column names?
import pandas as pd


def typeCol():
    data = pd.read_csv('04_gap-merged.tsv', sep='\t')
    print(data.dtypes)


# 5/ Get the country column and save it to its own variable. Show the first 5 observations.
# 6/ Show the last 5 observations of this column.
def getColCountry():
    with open('04_gap-merged.tsv', 'r') as file:
        # Initialize an empty list to store the country column
        country_column = []

        # Read the file line by line
        for line in file:
            columns = line.strip().split()  # Adjust the split method based on your file's format

            country = columns[0]
            country_column.append(country)
            if len(country_column) <= 6:
                print(country)

    country_variable = country_column
    for country in country_variable[-5:]:
        print(country)


# 7/ Look at country, continent and year. Show the first 5 observations of these columns, and the last 5 observations.
def cau7():
    with open('04_gap-merged.tsv', 'r') as file:
        # Khởi tạo các danh sách để lưu các cột
        country_column = []
        continent_column = []
        year_column = []

        # Đọc tập tin từng dòng một
        for line in file:
            # Tách dòng thành các cột
            columns = line.strip().split()  # Điều chỉnh phương thức split dựa trên định dạng của tập tin của bạn

            # Trích xuất thông tin về quốc gia, châu lục và năm
            country = columns[0]
            continent = columns[1]
            year = columns[2]

            # Thêm vào các cột tương ứng
            country_column.append(country)
            continent_column.append(continent)
            year_column.append(year)

    # Hiển thị 5 quan sát đầu tiên của mỗi cột
    print("5 dòng đầu tiên:")
    for i in range(6):
        print(f"Quốc gia: {country_column[i]}, Châu lục: {continent_column[i]}, Năm: {year_column[i]}")

    # Hiển thị 5 quan sát cuối cùng của mỗi cột
    print("\n5 dòng cuối cùng:")
    for i in range(-5, 0):
        print(f"Quốc gia: {country_column[i]}, Châu lục: {continent_column[i]}, Năm: {year_column[i]}")


# 8/ How to get the first row of tsv file? How to get the 100th row.
def cau8():
    # Lấy hàng thứ 100 của tập tin TSV
    with open('04_gap-merged.tsv', 'r') as file:
        for i in range(99):  # Đọc và loại bỏ 99 hàng đầu tiên
            file.readline()
        hundredth_row = file.readline().strip().split('\t')  # Đọc hàng thứ 100

    print("Hàng thứ 100 của tập tin TSV:", hundredth_row)


# 9/ Try to get the first column by using a integer index. And get the first and last column by passing the integer index.
def cau9():
    with open('04_gap-merged.tsv', 'r') as file:
        for line in file:
            columns = line.strip().split('\t')  # Giả sử tập tin TSV được phân tách bằng dấu tab
            if columns:  # Kiểm tra nếu dòng không rỗng
                columns.append(columns[0])

    print("Cột đầu tiên:", columns)


# 10/ How to get the last row with .loc? Try with index -1? Correct?
def cau10():
    df = pd.read_csv('04_gap-merged.tsv', sep='\t')

    # Lấy dòng cuối cùng bằng cách sử dụng .loc
    last_row = df.loc[df.index[-1]]

    print("Dòng cuối cùng sử dụng .loc:")
    print(last_row)


# 11/ How to select the first, 100th, 1000th rows by two methods?
def cau11():
    df = pd.read_csv('04_gap-merged.tsv', sep='\t')
    rows_iloc = df.iloc[[0, 99, 999]]

    print("Các hàng đã chọn sử dụng .iloc[]:")
    print(rows_iloc)
    # cách 2
    rows_loc = df.loc[[df.index[0], df.index[99], df.index[999]]]

    print("\nCác hàng đã chọn sử dụng .loc[]:")
    print(rows_loc)


# 12/ Get the 43rd country in our data using .loc, .iloc?
def cau12():
    df = pd.read_csv('04_gap-merged.tsv', sep='\t')

    # Lấy quốc gia thứ 43 bằng cách sử dụng .loc
    country_loc = df.loc[42, 'country']
    print("Quốc gia thứ 43 sử dụng .loc:", country_loc)
    # Lấy quốc gia thứ 43 bằng cách sử dụng .iloc
    country_iloc = df.iloc[42]['country']
    print("Quốc gia thứ 43 sử dụng .iloc:", country_iloc)


# 13/ How to get the first, 100th, 1000th rows from the first, 4th and 6th columns?
def cau13():
    df = pd.read_csv('04_gap-merged.tsv', sep='\t')

    # Chọn các hàng và cột bằng cách sử dụng .iloc
    rows_cols_iloc = df.iloc[[0, 99, 999], [0, 3, 5]]

    print("Các hàng và cột đã chọn sử dụng .iloc:")
    print(rows_cols_iloc)

    # Chọn các hàng và cột bằng cách sử dụng .loc
    rows_cols_loc = df.loc[[0, 99, 999], ['country', 'lifeExp', 'gdpPercap']]

    print("\nCác hàng và cột đã chọn sử dụng .loc:")
    print(rows_cols_loc)
# 14/ Get first 10 rows of our data (tsv file)?
def cau14():
    df = pd.read_csv('04_gap-merged.tsv', sep='\t')
    first_10_rows = df.head(10)
    print("First 10 rows of the data:")
    print(first_10_rows)
# 15/ For each year in our data, what was the average life expectation?
def cau15():
    df = pd.read_csv('04_gap-merged.tsv', sep='\t')

    # Tính trung bình của cột năm
    average_year = df['year'].mean()
    print("Trung bình của cột năm:", average_year)


# 16/ Using subsetting method for the solution of 15/?
# def cau16():

# 17/ Create a series with index 0 for ‘banana’ and index 1 for ’42’?
def cau17():
    s = pd.Series(['banana', '42'], index=[0, 1])
    print(s)


# 18/ Similar to 17, but change index ‘Person’ for ‘Wes MCKinney’ and index ‘Who’ for ‘Creator of Pandas’?
def cau18():
    s = pd.Series(['Wes McKinney', 'Creator of Pandas'], index=['Person', 'Who'])

    print(s)


# 19/ Create a dictionary for pandas with the data as ‘Occupation’: [’Chemist’, ’Statistician’], ’Born’: [’1920-07-25’, ’1876-06-13’],’Died’: [’1958-04-16’, ’1937-10-16’],’Age’: [37, 61] and the index is ‘Franklin’,’Gosset’ with four columns as indicated.
def cau19():
    data = {
        'Occupation': ['Chemist', 'Statistician'],
        'Born': ['1920-07-25', '1876-06-13'],
        'Died': ['1958-04-16', '1937-10-16'],
        'Age': [37, 61]
    }

    # Define the index
    index = ['Franklin', 'Gosset']

    # Create a DataFrame from the dictionary with specified index
    df = pd.DataFrame(data, index=index)

    print(df)


#PANDAS SEABORN
# 1/ Pandas Series is essentially a one-dimensional array, equipped with an index which labels its entries. We can create a Series object, for example, by converting a list (called diameters) [4879,12104,12756,6792,142984,120536,51118,49528]
# diameters=pd.Series([])
def func1():
    diameters_list = [4879, 12104, 12756, 6792, 142984, 120536, 51118, 49528]
    diameters = pd.Series(diameters_list)
    print(diameters)
# 2/ By default entries of a Series are indexed by consecutive integers, but we can specify a more meaningful index. The numbers in the above Series give diameters (in kilometers) of planets of the Solar System, so it is sensible to use names of the planet as index values:
# Index=[“Mercury”, “Venus”, “Earth”, “Mars”, “Jupyter”, “Saturn”, “Uranus”, “Neptune”]
# diameters=pd.Series([],index=[])
def func2():
    diameters_list = [4879, 12104, 12756, 6792, 142984, 120536, 51118, 49528]
    planet_names = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    diameters = pd.Series(diameters_list, index=planet_names)
    print(diameters)

    # 3/ Find diameter of Earth?diameters[“Earth”]
    earth_diameter = diameters["Earth"]
    print("Diameter of Earth:", earth_diameter)

if __name__ == '__main__':
    func1()
    func2()
    show_5line()
    numberRow_Col()
    printColName()
    typeCol()
    getColCountry()
    cau7()
    cau8()
    cau9()
    cau10()
    cau11()
    cau12()
    cau13()
    cau14()
    cau15()
    cau17()
    cau18()
    cau19()