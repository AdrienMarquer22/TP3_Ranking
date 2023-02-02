from ranking.ranking import Ranking

if __name__=="__main__":
    test=Ranking("chicago wikipédia",'or','bm25')
    test.load_index()
    test.load_documents()


    test.create_ranking()
    print(test.ranking)

    test.result()

    test.save_result('test.json')



