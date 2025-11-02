from transformers import pipeline

def summary_return(dat,summarizer):
  summary = summarizer(dat)[0]["summary_text"]
  return summary

def Summarization_out(inp_txt):
    my_model = r"C://Users//Shawon//Desktop//Defense Final//Model//"
    summarizer = pipeline("summarization", model = my_model)
    ans=summary_return(inp_txt,summarizer)
    return ans


'''
###Hardcoded Input
inp_txt="সপ্তাহের ব্যবধানে পেঁয়াজের দাম বৃদ্ধি পাওয়ায় খরচের অঙ্ক বাড়ল সংসারে।খুচরা পেঁয়াজ ব্যবসায়ীরা বলছেন, পাইকারিতে পেঁয়াজের দাম বেড়ে যাওয়ায় খুচরা পর্যায়েও দাম বেড়ে গেছে। বাজারে সরবরাহ কমে যাওয়ায় বাড়ছে মুরগির দাম।বাজারে পেঁয়াজ কিনতে এসে ক্রেতারা পড়ছেন বিপাকে"
out_txt=Summarization_out(inp_txt)
print("Summarized Output: \n", out_txt)
'''




###User Input
inp_txt = input("Give News: \n")
out_txt=Summarization_out(inp_txt)
print("Summarized Output: \n", out_txt)




 
'''
###File Input (Single news)
file_path = "C://Users//Shawon//Desktop//Defense Final//Codes//Output Code//"
inp_file = open(file_path + "input news.txt", "r", encoding="utf-8")
for x in inp_file:
    inp_txt = x

out_txt = Summarization_out(inp_txt)

out_file = open(file_path + "summarized news.txt", "w", encoding="utf-8")
out_file.write(out_txt)
out_file.close()
'''








'''
###File Input (Multiple news)
file_path = "C://Users//Shawon//Desktop//Defense Final//Codes//Output Code//"
inp_file = open(file_path + "input news.txt", "r", encoding="utf-8")

out_file = open(file_path + "summarized news.txt", "w", encoding="utf-8")
out_file.write("")
out_file.close()

out_file = open(file_path + "summarized news.txt", "a", encoding="utf-8")

while True:
    inp_txt = inp_file.readline()
    if (len(inp_txt) == 0):
        break
    if (len(inp_txt) > 1):
        out_txt = "News:\n" + inp_txt + "Headline:\n" + Summarization_out(inp_txt) + "\n" + "\n" + "\n" + "\n"
        out_file.write(out_txt)
        
out_file.close()
 

'''




print("Done")











