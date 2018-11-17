#! - * - coding: utf8 - * -
'''
Created on 2018/11/14

@author: xkzm
'''

import csv


if __name__ == '__main__':
    sep = u"|"
    with open("../resource/LDBCSNB/comment_0_0.csv", "r", encoding = "utf-8") as f:
        reader = csv.reader(f, delimiter = sep)
        header = next(reader)
        header_str = sep.join([header[0] + ":ID", \
                               header[1] + ":datetime", \
                               header[2] + ":string", \
                               header[3] + ":string", \
                               header[4] + ":string", \
                               header[5] + ":int", \
                                           ":LABEL"])
                               
        with open("../resource/neo4j/node_comment.csv", "w", encoding = "utf-8") as out:
            row6 = open("../resource/neo4j/rel_comment-creator.csv",        "w", encoding = "utf-8")
            row7 = open("../resource/neo4j/rel_comment-place.csv",          "w", encoding = "utf-8")
            row8 = open("../resource/neo4j/rel_comment-replyOfPost.csv",    "w", encoding = "utf-8")
            row9 = open("../resource/neo4j/rel_comment-replyOfComment.csv", "w", encoding = "utf-8")
            row6.write(sep.join([":START_ID", ":END_ID", ":TYPE"]) + "\n")
            row7.write(sep.join([":START_ID", ":END_ID", ":TYPE"]) + "\n")
            row8.write(sep.join([":START_ID", ":END_ID", ":TYPE"]) + "\n")
            row9.write(sep.join([":START_ID", ":END_ID", ":TYPE"]) + "\n")
            out.write(header_str + "\n")
            for row in reader:
                out.write(sep.join(row[0:6] + ["Comment"]) + "\n")
                if row[6] != "": row6.write(sep.join([row[0], row[6], "creator"])        + "\n")
                if row[7] != "": row7.write(sep.join([row[0], row[7], "place"])          + "\n")
                if row[8] != "": row8.write(sep.join([row[0], row[8], "replyOfPost"])    + "\n")
                if row[9] != "": row9.write(sep.join([row[0], row[9], "replyOfComment"]) + "\n")
            
            row6.close()
            row7.close()
            row8.close()
            row9.close()

    with open("../resource/LDBCSNB/comment_hasTag_tag_0_0.csv", "r", encoding = "utf-8") as f:
        reader = csv.reader(f, delimiter = sep)
        header = next(reader)
        header_str = sep.join([":START_ID", ":END_ID", ":TYPE"])
                               
        with open("../resource/neo4j/rel_comment-hasTag.csv", "w", encoding = "utf-8") as out:
            out.write(header_str + "\n")
            for row in reader:
                out.write(sep.join(row[:2] + ["hasTag"]) + "\n")

    with open("../resource/LDBCSNB/forum_0_0.csv", "r", encoding = "utf-8") as f:
        reader = csv.reader(f, delimiter = sep)
        header = next(reader)
        header_str = sep.join([header[0] + ":ID", \
                               header[1] + ":string", \
                               header[2] + ":datetime", \
                                           ":LABEL"])
                               
        with open("../resource/neo4j/node_forum.csv", "w", encoding = "utf-8") as out:
            row3 = open("../resource/neo4j/rel_forum-moderator.csv", "w", encoding = "utf-8")
            row3.write(sep.join([":START_ID", ":END_ID", ":TYPE"]) + "\n")
            out.write(header_str + "\n")
            for row in reader:
                out.write(sep.join(row[0:3] + ["Forum"]) + "\n")
                if row[3] != "": row3.write(sep.join([row[0], row[3], "moderator"]) + "\n")
            
            row3.close()

    with open("../resource/LDBCSNB/forum_hasMember_person_0_0.csv", "r", encoding = "utf-8") as f:
        reader = csv.reader(f, delimiter = sep)
        header = next(reader)
        header_str = sep.join([":START_ID", ":END_ID", ":TYPE", header[2] + ":datetime"])
                               
        with open("../resource/neo4j/rel_forum-hasMember.csv", "w", encoding = "utf-8") as out:
            out.write(header_str + "\n")
            for row in reader:
                out.write(sep.join(row[:2] + ["hasMember", header[2]]) + "\n")

    with open("../resource/LDBCSNB/forum_hasTag_tag_0_0.csv", "r", encoding = "utf-8") as f:
        reader = csv.reader(f, delimiter = sep)
        header = next(reader)
        header_str = sep.join([":START_ID", ":END_ID", ":TYPE"])
                               
        with open("../resource/neo4j/rel_forum-hasTag.csv", "w", encoding = "utf-8") as out:
            out.write(header_str + "\n")
            for row in reader:
                out.write(sep.join(row[:2] + ["hasTag"]) + "\n")

    with open("../resource/LDBCSNB/organisation_0_0.csv", "r", encoding = "utf-8") as f:
        reader = csv.reader(f, delimiter = sep)
        header = next(reader)
        header_str = sep.join([header[0] + ":ID", \
                               header[1] + ":string", \
                               header[2] + ":string", \
                               header[3] + ":string", \
                                           ":LABEL"])
                               
        with open("../resource/neo4j/node_organisation.csv", "w", encoding = "utf-8") as out:
            row4 = open("../resource/neo4j/rel_organisation-place.csv", "w", encoding = "utf-8")
            row4.write(sep.join([":START_ID", ":END_ID", ":TYPE"]) + "\n")
            out.write(header_str + "\n")
            for row in reader:
                out.write(sep.join(row[0:4] + ["Organisation"]) + "\n")
                if row[4] != "": row4.write(sep.join([row[0], row[4], "place"]) + "\n")
            
            row4.close()

    with open("../resource/LDBCSNB/person_0_0.csv", "r", encoding = "utf-8") as f:
        reader = csv.reader(f, delimiter = sep)
        header = next(reader)
        header_str = sep.join([header[0]  + ":ID", \
                               header[1]  + ":string", \
                               header[2]  + ":string", \
                               header[3]  + ":string", \
                               header[4]  + ":datetime", \
                               header[5]  + ":datetime", \
                               header[6]  + ":string", \
                               header[7]  + ":string", \
                               "language" + ":string[]", \
                               "email"    + ":string[]", \
                                            ":LABEL"])
                               
        pid2lang = {}
        with open("../resource/LDBCSNB/person_speaks_language_0_0.csv", "r", encoding = "utf-8") as f:
            reader_pl = csv.reader(f, delimiter = sep)
            header = next(reader_pl)
            for row in reader_pl:
                if row[0] in pid2lang.keys():
                    pid2lang[row[0]].append(row[1])
                else:
                    pid2lang[row[0]] = [row[1]]

        pid2email = {}
        with open("../resource/LDBCSNB/person_email_emailaddress_0_0.csv", "r", encoding = "utf-8") as f:
            reader_pe = csv.reader(f, delimiter = sep)
            header = next(reader_pe)
            for row in reader_pe:
                if row[0] in pid2email.keys():
                    pid2email[row[0]].append(row[1])
                else:
                    pid2email[row[0]] = [row[1]]
                        
        with open("../resource/neo4j/node_person.csv", "w", encoding = "utf-8") as out:
            row8 = open("../resource/neo4j/rel_person-place.csv", "w", encoding = "utf-8")
            row8.write(sep.join([":START_ID", ":END_ID", ":TYPE"]) + "\n")
            out.write(header_str + "\n")
            for row in reader:
                langs  = ";".join(pid2lang [row[0]])
                emails = ";".join(pid2email[row[0]])
                out.write(sep.join(row[0:8] + [langs, emails, "Person"]) + "\n")
                if row[8] != "": row8.write(sep.join([row[0], row[8], "place"]) + "\n")
            
            row8.close()

    with open("../resource/LDBCSNB/person_hasInterest_tag_0_0.csv",      "r", encoding = "utf-8") as f:
        reader = csv.reader(f, delimiter = sep)
        header = next(reader)
        header_str = sep.join([":START_ID", ":END_ID", ":TYPE"])
                               
        with open("../resource/neo4j/rel_person_hasInterest.csv", "w", encoding = "utf-8") as out:
            out.write(header_str + "\n")
            for row in reader:
                out.write(sep.join(row[:2] + ["hasInterest"]) + "\n")

    with open("../resource/LDBCSNB/person_knows_person_0_0.csv",         "r", encoding = "utf-8") as f:
        reader = csv.reader(f, delimiter = sep)
        header = next(reader)
        header_str = sep.join([":START_ID", ":END_ID", ":TYPE", "creationDate:datetime"])
                               
        with open("../resource/neo4j/rel_person_knows.csv", "w", encoding = "utf-8") as out:
            out.write(header_str + "\n")
            for row in reader:
                out.write(sep.join(row[:2] + ["creationDate", row[2]]) + "\n")

    with open("../resource/LDBCSNB/person_likes_comment_0_0.csv",        "r", encoding = "utf-8") as f:
        reader = csv.reader(f, delimiter = sep)
        header = next(reader)
        header_str = sep.join([":START_ID", ":END_ID", ":TYPE", "creationDate:datetime"])
                               
        with open("../resource/neo4j/rel_person_likes.csv", "w", encoding = "utf-8") as out:
            out.write(header_str + "\n")
            for row in reader:
                out.write(sep.join(row[:2] + ["creationDate", row[2]]) + "\n")
        
    with open("../resource/LDBCSNB/person_likes_post_0_0.csv", "r", encoding = "utf-8") as f:
        reader = csv.reader(f, delimiter = sep)
        header = next(reader)
        header_str = sep.join([":START_ID", ":END_ID", ":TYPE", "creationDate:datetime"])
                               
        with open("../resource/neo4j/rel_person_likes.csv", "a", encoding = "utf-8") as out:
            out.write(header_str + "\n")
            for row in reader:
                out.write(sep.join(row[:2] + ["creationDate", row[2]]) + "\n")
        

    with open("../resource/LDBCSNB/person_studyAt_organisation_0_0.csv", "r", encoding = "utf-8") as f:
        reader = csv.reader(f, delimiter = sep)
        header = next(reader)
        header_str = sep.join([":START_ID", ":END_ID", ":TYPE", "classYear:int"])
                               
        with open("../resource/neo4j/rel_person_studyAt.csv", "w", encoding = "utf-8") as out:
            out.write(header_str + "\n")
            for row in reader:
                out.write(sep.join(row[:2] + ["studyAt", row[2]]) + "\n")
        
    with open("../resource/LDBCSNB/person_workAt_organisation_0_0.csv",  "r", encoding = "utf-8") as f:
        reader = csv.reader(f, delimiter = sep)
        header = next(reader)
        header_str = sep.join([":START_ID", ":END_ID", ":TYPE", "workFrom:int"])
                               
        with open("../resource/neo4j/rel_person_workAt.csv", "w", encoding = "utf-8") as out:
            out.write(header_str + "\n")
            for row in reader:
                out.write(sep.join(row[:2] + ["workAt", row[2]]) + "\n")
        
    with open("../resource/LDBCSNB/place_0_0.csv", "r", encoding = "utf-8") as f:
        reader = csv.reader(f, delimiter = sep)
        header = next(reader)
        header_str = sep.join([header[0] + ":ID", \
                               header[1] + ":string", \
                               header[2] + ":string", \
                               header[3] + ":string", \
                                           ":LABEL"])
                               
        with open("../resource/neo4j/node_place.csv", "w", encoding = "utf-8") as out:
            row4 = open("../resource/neo4j/rel_place_isPartOf.csv", "w", encoding = "utf-8")
            row4.write(sep.join([":START_ID", ":END_ID", ":TYPE"]) + "\n")
            out.write(header_str + "\n")
            for row in reader:
                out.write(sep.join(row[0:4] + ["Place"]) + "\n")
                if row[4] != "": row4.write(sep.join([row[0], row[4], "isPartOf"]) + "\n")
            
            row4.close()

    with open("../resource/LDBCSNB/post_0_0.csv",                        "r", encoding = "utf-8") as f:
        reader = csv.reader(f, delimiter = sep)
        header = next(reader)
        header_str = sep.join([header[0] + ":" + "ID", \
                               header[1] + ":" + "string", \
                               header[2] + ":" + "datetime", \
                               header[3] + ":" + "string", \
                               header[4] + ":" + "string", \
                               header[5] + ":" + "string", \
                               header[6] + ":" + "string", \
                               header[7] + ":" + "int", \
                                           ":LABEL"])
                               
        with open("../resource/neo4j/node_post.csv", "w", encoding = "utf-8") as out:
            row8  = open("../resource/neo4j/rel_post_creator.csv", "w", encoding = "utf-8")
            row9  = open("../resource/neo4j/rel_post_forum.csv",   "w", encoding = "utf-8")
            row10 = open("../resource/neo4j/rel_post_place.csv",   "w", encoding = "utf-8")
            row8 .write(sep.join([":START_ID", ":END_ID", ":TYPE"]) + "\n")
            row9 .write(sep.join([":START_ID", ":END_ID", ":TYPE"]) + "\n")
            row10.write(sep.join([":START_ID", ":END_ID", ":TYPE"]) + "\n")
            out.write(header_str + "\n")
            for row in reader:
                out.write(sep.join(row[0:8] + ["Post"]) + "\n")
                if row[ 8] != "": row8. write(sep.join([row[0], row[ 8], "creator"]) + "\n")
                if row[ 9] != "": row9. write(sep.join([row[0], row[ 9], "forum"  ]) + "\n")
                if row[10] != "": row10.write(sep.join([row[0], row[10], "place"  ]) + "\n")
            
            row8 .close()
            row9 .close()
            row10.close()

    with open("../resource/LDBCSNB/post_hasTag_tag_0_0.csv", "r", encoding = "utf-8") as f:
        reader = csv.reader(f, delimiter = sep)
        header = next(reader)
        header_str = sep.join([":START_ID", ":END_ID", ":TYPE"])
                               
        with open("../resource/neo4j/rel_person_hasTag.csv", "w", encoding = "utf-8") as out:
            out.write(header_str + "\n")
            for row in reader:
                out.write(sep.join(row[:2] + ["hasTag"]) + "\n")
        
    with open("../resource/LDBCSNB/tag_0_0.csv", "r", encoding = "utf-8") as f:
        reader = csv.reader(f, delimiter = sep)
        header = next(reader)
        header_str = sep.join([header[0] + ":ID", \
                               header[1] + ":string", \
                               header[2] + ":string", \
                                           ":LABEL"])
                               
        with open("../resource/neo4j/node_tag.csv", "w", encoding = "utf-8") as out:
            row3 = open("../resource/neo4j/rel_tag_hasType.csv", "w", encoding = "utf-8")
            row3.write(sep.join([":START_ID", ":END_ID", ":TYPE"]) + "\n")
            out.write(header_str + "\n")
            for row in reader:
                out.write(sep.join(row[0:3] + ["Tag"]) + "\n")
                if row[3] != "": row3. write(sep.join([row[0], row[3], "hasType"]) + "\n")
            
            row3.close()

    with open("../resource/LDBCSNB/tagclass_0_0.csv", "r", encoding = "utf-8") as f:
        reader = csv.reader(f, delimiter = sep)
        header = next(reader)
        header_str = sep.join([header[0] + ":ID", \
                               header[1] + ":string", \
                               header[2] + ":string", \
                                           ":LABEL"])
                               
        with open("../resource/neo4j/node_tagclass.csv", "w", encoding = "utf-8") as out:
            row3 = open("../resource/neo4j/rel_tagclass_isSubclassOf.csv", "w", encoding = "utf-8")
            row3.write(sep.join([":START_ID", ":END_ID", ":TYPE"]) + "\n")
            out.write(header_str + "\n")
            for row in reader:
                out.write(sep.join(row[0:3] + ["Tagclass"]) + "\n")
                if row[3] != "": row3.write(sep.join([row[0], row[3], "isSubclassOf"]) + "\n")
            
            row3.close()
