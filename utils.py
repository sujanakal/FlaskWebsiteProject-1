# import Blogpost
# from flask_sqlalchemy import SQLAlchemy 

def getBlogPosts():
    blog_posts = [{
    'title' : 'Blah blah',
    'posted_on' : 'yesterday',
    'content' : 'Blah blah Blah blah Blah blah Blah blah'
},
{
    'title' : 'Blah blah',
    'posted_on' : 'yesterday',
    'content' : 'Blah blah Blah blah Blah blah Blah blah'
},
 {
    'title' : 'Blah blah',
    'posted_on' : 'yesterday',
    'content' : 'Blah blah Blah blah Blah blah Blah blah'
    }
]

    # cursor = Blogpost.query.all()
    # response_data = []
    # for row in cursor:
    #     temp_data = {
    #         'title': row.title,
    #         'posted_on':row.posted_on,
    #         'comments':row.comments,
    #         'content':row.content
    #     }
    #     response_data.append(temp_data)

    return blog_posts