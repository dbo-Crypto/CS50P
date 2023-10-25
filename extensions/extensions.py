user_input = input("File name: ")
extension = user_input.lower().strip().split(".")[-1]


match extension:
    case "gif" | "png":
        print("image/"+extension)
    case "jpg" | "jpeg":
        print("image/jpeg")
    case "txt":
        print("text/plain")
    case "bin":
        print("application/octet-stream")
    case "pdf":
        print("application/pdf")
    case "zip":
        print("application/zip")
    case _:
        print("application/octet-stream")