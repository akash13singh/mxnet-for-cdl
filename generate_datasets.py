import random
import csv


# divides users.dat into training and test set. P denotes the number of articles used for test set. P=1 sparse setting. P =10 dense setting. Default is dense setting
def create_training_test_sets(P=10,n=5551):
    train = [[] for _dummy in xrange(n)]
    test = [[] for _dummy in xrange(n)]
    fp= open("users.dat")
    users = fp.readlines()
    num_users = len(users)
    for user_id in range(num_users):
        entry =  users[user_id]
        entry = entry.split(" ")
        num_articles = int(entry[0])
        articles = entry[1:]

        train_idx = random.sample(xrange(num_articles),P)

        train[user_id].append(P)
        test[user_id].append(num_articles-P)

        for i in range(num_articles):

            if i in train_idx:
                train[user_id].append(int(articles[i]))
            else:
                test[user_id].append(int(articles[i]))

    return train,test



def generate_datasets(num_samples,num_sets=1,setting="dense",):
    if setting == "dense":
        P = 10
    else:
        P = 1
    random.seed(1234)
    for i in range(num_sets):


        train,test = create_training_test_sets(P,num_samples )
        trainFile = "data/train_P"+str(P)+"_"+str(i+1)+".dat"
        testFile = "data/test_P"+str(P)+"_"+str(i+1)+".dat"

        with open(trainFile, "wb") as f:
            writer = csv.writer(f, delimiter=' ')
            writer.writerows(train)

        with open(testFile, "wb") as f:
            writer = csv.writer(f, delimiter=' ')
            writer.writerows(test)


if __name__ == '__main__':
    generate_datasets(num_samples=5551,num_sets=3,setting="sparse")
