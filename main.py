from ranking.ranking import Ranking
import argparse
if __name__=="__main__":
    # test=Ranking("chicago wikipédia",'or','bm25')
    # test.load_index()
    # test.load_documents()


    # test.create_ranking()
    # #print(test.ranking)

    # test.result()

    # test.save_result('test.json')

    parser = argparse.ArgumentParser()
    parser.add_argument('--request')
    parser.add_argument('--name',default="result")
    parser.add_argument('--type',default="and")

    parser.add_argument('--linear', action='store_true',default=False)

    parser.add_argument('--bm25', action='store_true',default=False)

    args = parser.parse_args()

    if args.linear : 
        ranking=Ranking(args.request,args.type,'linear')
        ranking.load_index()
        ranking.load_documents()
        ranking.create_ranking()
        ranking.result()
        if args.bm25 : 
            ranking.save_result(args.name + '_linear.json')
        else:
            ranking.save_result(args.name + '.json')

    if args.bm25:
        ranking=Ranking(args.request,args.type,'bm25')
        ranking.load_index()
        ranking.load_documents()
        ranking.create_ranking()
        ranking.result()
        if args.linear : 
            ranking.save_result(args.name + '_bm25.json')
        else:
            ranking.save_result(args.name + '.json')









