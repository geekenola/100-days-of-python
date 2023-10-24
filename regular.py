

text = """We are hiring: Senior Software Engineer - Proto http://www.reqcloud.com/jobs/719865/?k=0LaPxXuFwczs1e32ZURJKrgCIDMQtRO7BquFSQthUKY&utm_source=twitter&utm_campaign=reqCloud_JobPost #job @awscloud #job #protocol #networking #aws #mediastreaming
RT @CodeMineStatus: This is true Amazon Web Services https://aws.amazon.com/ #php #html #html5 #css #webdesign #seo #java #javascript htt
Devops Engineer Aws Ansible Cassandra Mysql Ubuntu Ruby On Rails Jobs in Austin TX #Austin #TX #jobs #jobsearch https://www.jobfindly.com/devops-engineer-aws-ansible-cassandra-mysql-ubuntu-ruby-on-rails-jobs-austin-tx.html
Happy New Year to all those AWS instances of ours!
Amazon is hiring! #Sr. #International Tax Manager - AWS in #Seattle apply now! #jobs http://neuvoo.com/job.php?id=dsvkrujig3&source=twitter&lang=en&client_id=658&l=Seattle%20Washington%20US&k=Sr.%20International%20Tax%20Manager%20-%20AWS http://twitter.com/NeuvooAccSea/status/682714048199311366/photo/1
#AWS bc of per-region limits test/prod should be in isolated regions. else dev could impact prod #lambda &amp; beyond http://docs.aws.amazon.com/lambda/latest/dg/limits.html#limits-safety-throttles
Isolating dev/prod #aws envs like that is difficult bc of non-ubiquitous service availability. Isn't really a good way around this problem.
Isolation at account level would work. #aws alludes to this on pg 17 but this makes identity management difficult http://media.amazonwebservices.com/AWS_Security_Best_Practices.pdf
Red line vs. green line: Reporting on the most vital Reserved Instance metrics: http://blog.cloudability.com/red-line-vs-green-line-reporting-on-reserved-instance-coverage-and-waste/ #AWS http://twitter.com/cloudability/status/682717967965110273/photo/1
RT @HPE_BigData: We developed a test drive on AWS. Why is it worth trying? @waltermaguire explains: http://community.hpe.com/t5/Big-Data/Don-t-build-the-car-for-a-test-drive-Evaluate-faster-with-the/ba-p/6819020 #BigData https:
RT @awscloud: AWS CloudFormation now supports AWS WAF &amp; AWS Directory Service for MS Active Directory. https://aws.amazon.com/about-aws/whats-new/2015/12/aws-cloudformation-adds-support-for-aws-waf-and-aws-directory-service-for-microsoft-active-directory/?sc_channel=sm&sc_campaign=launches&sc_publisher=tw_go&sc_content=waf_ds&sc_country=global&sc_geo=global&sc_category=cloudformation&adbsc=social_launches_20151228_56779066&adbid=681570169089429504&adbpl=tw&adbpr=66780587 https://t.co
"""


def extract_hashtags(text):
    words = text.split()
    hashtags = []
    for word in words:
        if word.startswith('#'):
            hashtags.append(word)
    return hashtags


def replace_rt(text):
    words = text.split()
    updated_words = []
    for word in words:
        if word == 'RT':
            updated_words.append('ReTweeted')
        else:
            updated_words.append(word)
    return ' '.join(updated_words)


hashtags_list = extract_hashtags(text)


updated_text = replace_rt(text)


print("List of Hashtags:")
print(hashtags_list)
print("\nUpdated Text:")
print(updated_text)
