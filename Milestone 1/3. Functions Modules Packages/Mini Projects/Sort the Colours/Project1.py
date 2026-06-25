def sort_colors(colors):
    color_list=colors.split("-")
    color_list.sort()
    return "-".join(color_list)

colors=input("Enter colors: ")
print(sort_colors(colors))