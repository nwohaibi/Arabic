__author__ = 'd7eame'

particles = ('في', 'عن', 'إلى', 'على')
particles2 = ('ب')
zarf = (
    'قبل', 'بعد', 'فوق', 'تحت', 'بين', 'خلف', 'يمين', 'يسار', 'وراء', 'مع', 'أمام', 'حول', 'عند', 'قدام', 'إزاء',
    'جوار',
    'نحو')
kana_sisters = ('كان', 'يكون', 'كن', 'أصبح', 'يصبح', 'أضحى', 'بات', 'يبيت', 'بت', 'أمسى', 'يمسي', 'صار', 'يصير', 'صر',
                'ليس')  # ما انفك، ما برح، ما زال، ما دام، ما فتئ، ظل مشكلة
enna_sisters = ('إن', 'أن', 'لكن', 'ليت', 'لعل', 'كأن')
mudhar3 = ('أن', 'لن', 'كي', 'إذن', 'لم', 'لما')
# anit = ('أ', 'ن', 'ي', 'ت')
ti = ('ت', 'ي')
tarqim = (
'.', ':', '!', '؟', '،', '؛', '"', "'", '"', ',', '-', '*', ')', '(', '”', '»', '«', '“', '–', 'a', 'b', 'c', 'd', 'e',
'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '(', ')', '[',
']', '{', '}', '&', '$', '#', '@', '<', '>', '/', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '=', ';', '|', 'A',
'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
'Z', '_')
# as you can see in the exceptions list, I write the word twice. one with ال and one without and this is due to my lack in programming skills.
exceptions = (
    'بلدان', 'قرآن', 'بروتون', 'البلدان', 'البروتون', 'القرآن', 'القرون', 'حمدان', 'الحمدان', 'تلمسان', 'بوتان', 'سجون',
    'السجون', 'حصان', 'الحصان', 'بيرتان', 'القران', 'فرعون', 'الفرعون', 'سريان', 'السريان', 'الحصون', 'السكان', 'سكان',
    'طليان',
    'الطليان', 'أمريكان', 'الأمريكان', 'دوران', 'الدوران', 'إيران', 'طهران', 'اللسان', 'عمران', 'العمران', 'الجنان',
    'لوران', 'الأمان', 'ثوران', 'الثوران', 'إخوان', 'الإخوان', 'بورون', 'البورون', 'الأذان', 'ميلان', 'الميلان',
    'حيتان',
    'الحيتان', 'الغصون', 'ألوان', 'الألوان', 'توران', 'الكمان', 'لبنان', 'نيسان', 'المكان', 'عبدون', 'اللجان', 'أركان',
    'الأركان', 'طالبان', 'اللون', 'سليمان', 'عدوان', 'العدوان', 'سودان', 'السودان', 'شارون', 'يعاون', 'الجبان',
    'الدهون', 'الشريان', 'النيران', 'نيران',
    'شريان', 'إيلان', 'ميسان', 'فرحان', 'الفرحان', 'العون', 'هامان', 'تبيان', 'شعبان', 'شبعان', 'قولون', 'هيمان',
    'الهيمان', 'الشبعان', 'القولون', 'التبيان', 'ألحان', 'الألحان', 'ألمان', 'سلمون', 'السلمون', 'بركان', 'البركان',
    'براون', 'بعدان', 'بيجان', 'الجنون', '', '',
    'بوسان',
    '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '')
exceptions2 = ('الاثنين', 'ياسين', '', '', '', '', '', '', '', '')

f3l = []
yen = []
an = []
won = []

with open("d.txt", "r", encoding='utf-8') as myfile:
    string = myfile.read()
    for i in range(len(tarqim)):
        string = string.replace(tarqim[i], ' ')


def split_string(string):
    words = string.split()
    return words


def a3rb(words, f3l, won, yen, an):
    c = 0  #number of corrections
    for i in range(len(words)):
        x = i  #number of words scanned
        #works perfectly even without the exceptions due to the six explicit conditions. نصب وجزم الأفعال الخمسة
        if ((words[i][-2:] == "ون") or (words[i][-2:] == "ان") or (words[i][-2:] == 'ين')) and words[i][
                                                                                               0:2] != 'ال' and len(
                words[i][1:-2]) >= 3 and words[i][0] in ti and words[i - 1] in mudhar3 and words[
            i] not in exceptions and words[i][1:-2] in f3l:
            print('قبل:', words[i - 1], words[i])  # for testing
            if words[i][-2:] == 'ان':
                words[i] = words[i][0:-1]
            elif words[i][-2:] == 'ون':
                words[i] = words[i][0:-1] + 'ا'
            elif words[i][-2:] == 'ين':
                words[i] = words[i][0:-1]
            print('بعد:', words[i - 1], words[i], '(أفعال خمسة)')  # for testing
            c += 1

        elif ((words[i][-2:] == "ون") or (words[i][-2:] == "ان")) and (len(words[i]) > 4) and (
            words[i] not in exceptions) and ((words[i][0:-2] + 'ين') in yen):  # الخفض للمثنى وجمع المذكر السالم
            if words[i - 1] in particles:  # لجر الاسماء المجرورة بحروف الجر المنفصلة
                print('قبل:', words[i - 1], words[i])  #for testing
                if words[i][-2:] == 'ان':
                    words[i] = words[i][0:-2] + 'يَن'
                else:
                    words[i] = words[i][0:-2] + 'ين'
                print('بعد:', words[i - 1], words[i], '(حرف جر منفصل)')  #for testing
                c += 1

            elif words[i][0] in particles2 and words[i][1:] not in exceptions and (
                    words[i][1:] in yen or words[i][1:] in an):  #لجر الاسماء المجرورة بحروف الجر المتصلة
                print('قبل:', words[i - 1], words[i])  #for testing
                if words[i][-2:] == 'ان':
                    words[i] = words[i][0:-2] + 'يَن'
                else:
                    words[i] = words[i][0:-2] + 'ين'
                print('بعد:', words[i - 1], words[i], '(حرف جر متصل)')  #for testing
                c += 1

            elif words[i - 2] in kana_sisters and words[i][0:2] != 'ال' and words[i][
                                                                            0:2] != 'وال':  #نصب خبر كان وأخواتها
                print('قبل:', words[i - 2], words[i - 1], words[i])  #for testing
                if words[i][-2:] == 'ان':
                    words[i] = words[i][0:-2] + 'يَن'
                else:
                    words[i] = words[i][0:-2] + 'ين'
                print('بعد:', words[i - 2], words[i - 1], words[i], '(نصب كان)')  #for testing
                c += 1

            elif words[i - 1] in enna_sisters:  #نصب اسم إن وأخواتها
                print('قبل:', words[i - 1], words[i], words[i + 1])  #for testing
                if words[i][-2:] == 'ان':
                    words[i] = words[i][0:-2] + 'يَن'
                else:
                    words[i] = words[i][0:-2] + 'ين'
                print('بعد:', words[i - 1], words[i], words[i + 1], '(نصب إن)')  #for testing
                c += 1

            elif words[i - 1] in zarf:  #expeirmental - بعد ظرف المكان أو الزمان
                print('قبل:', words[i - 1], words[i])  #for testing
                if words[i][-2:] == 'ان':
                    words[i] = words[i][0:-2] + 'يَن'
                else:
                    words[i] = words[i][0:-2] + 'ين'
                print('بعد:', words[i - 1], words[i], '(ظرف)')  #for testing
                c += 1

            elif False and words[i - 1][-1] == 'ت' and len(words[i - 1]) > 3 and len(words[i - 1]) <= 5 and words[i][
                -3] != 'ت' and words[i - 1][
                               0:-1] in f3l:  #Expeirmental - alpha #More processing - مفعول به، يبحث في الفعل الثلاثي والرباعي فقط
                print('قبل:', words[i - 1], words[i])  #for testing
                if words[i][-2:] == 'ان':
                    words[i] = words[i][0:-2] + 'يَن'
                else:
                    words[i] = words[i][0:-2] + 'ين'
                print('بعد:', words[i - 1], words[i], '(مفعول)')  #for testing
                c += 1

                #الرفع للمثنى وجمع المذكر السالم
                # الرفع مشكلته مشكلة بسبب صعوبة التفريق بين المثنى وجمع المذكر السالم في حالة الخفض إذا كانت الكلمة غير مشكلة. فمعلمين قد تكون مثنى وقد تكون جمع، ما أحاول أن أقوم به هنا هو رفع المثنى الذي جمعه جمع تكسير
                # ستكون النتيجة خاطئة في حالة واحدة فقط، وهي عندما تكون الكلمة جمع مذكر سالم ولكنه ليس موجود بحالته المرفوعة في الموسوعة وكلها ويوجد بحالته المرفوعة وهو مثنى، وهذا نادر الحدوث بالذات مع ميل
        elif (words[i][-2:] == 'ين') and len(words[i]) >= 5 and (words[i] not in exceptions2) and (
            (words[i][0:-2] + 'ون') not in won) and ((words[i][0:-2] + 'ان') in an):
            if words[i - 1] in kana_sisters:  # رفع اسم كان وأخواتها
                print('قبل:', words[i - 1], words[i], words[i + 1])  #for testing
                words[i] = words[i][0:-2] + 'ان'
                print('بعد:', words[i - 1], words[i], words[i + 1], '(رفع كان)')  #for testing
                c += 1

            elif words[i - 2] in enna_sisters and words[i][0:2] != 'ال' and words[i][
                                                                            0:2] != 'وال':  #رفع خبر إن وأخواتها عندما يكون مثنى
                print('قبل:', words[i - 2], words[i - 1], words[i])  #for testing
                words[i] = words[i][0:-2] + 'ان'
                print('بعد:', words[i - 2], words[i - 1], words[i], '(رفع إن)')  #for testing
                c += 1

    print('Number of words =', x)
    print('Number of corrections =', c)


words = split_string(string)

#to make the code faster
for i in range(len(words)):
    if (len(words[i]) == 3 or len(words[i]) == 4) and (words[i] not in f3l):
        f3l.append(words[i])
    if (words[i] not in exceptions) and (words[i] not in exceptions2):
        if (words[i][-2:] == 'ين') and (words[i] not in yen):
            yen.append(words[i])
        elif (words[i][-2:] == "ون") and (words[i] not in won):
            won.append(words[i])
        elif (words[i][-2:] == "ان") and (words[i] not in an):
            an.append(words[i])
print(i)

a3rb(words, f3l, won, yen, an)

# هناك مساحة للتطوير بالذات عندما يكون الاسم مضافًا مثل يا معلمو المدرسة والصحيح يا معلمي المدرسة
#We can improve the search function by stripping the ال from the word first and then search for it. Or adding ال to it if it does not have one. But I don't think it's necessary since the data base is huge.
#if the word is at the beginning of a sentence then it should be
