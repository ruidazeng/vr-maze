import os
import traceback
rootdir = 'C:/Navigation Data/Labeled'
works = 0
no_works = 0

for subdir, dirs, files in os.walk(rootdir):
    try:
        for infile in files:
            if "CW4Test_Data" in infile:
                target_file = infile
            else:
                continue

            prev = 0
            started = False
            index = 0
            printed = 0
            # search for the magic 10 minutes
            with open(os.path.join(subdir, target_file)) as openfileobject:
                for line in openfileobject:
                    # skip blank lines
                    if line == '\n': continue
                    datetime = line.split('\t')[0]
                    num = float(line.split('\t')[1])
                    # print(num)
                    if index == 0: # blank line
                        prev = num
                        index += 1
                        continue
                    # this code also ensures only around-10 minutes intervals are printed
                    if abs(num - prev) > 1.00:
                        if not started:
                            tracker = num
                            start_index = index
                            start_datetime = datetime
                            start_prev = prev
                            start_num = num
                        else:
                            if abs(prev - tracker) > 200 and abs(prev - tracker) < 700:
                                printed += 1
                        started = not started
                    prev = num
                    index += 1


            # additional tracker
            if printed > 1:
                works += 1
                print('works:', subdir.split('\\')[1])
            else:
                no_works += 1
                print('doesnt works:', subdir.split('\\')[1])
    except:
        no_works += 1
        print('exception detected:', subdir.split('\\')[1])
        print('\n', traceback.format_exc())



print('we successfully found a unique candidate for', works, 'files')
print('we failed to find a unique candidate for', no_works, 'files')
# print('success rate:', round(works/(works + no_works), 4))

