
class vars():
    def env(enve):
        if enve=='dev':
            BW_dir='https://10.170.121.120'
            Mashery_dir='https://services-dev.br.xcd.net.intra/'
        if enve=='uat':
            BW_dir='https://10.170.121.119'
            Mashery_dir='https://api-services-uat.cardifnet.com/'
        if enve=='prd':
            BW_dir='https://10.170.121.115'
            Mashery_dir='https://api-services.cardifnet.com/'
        if enve=='qa':
            BW_dir='https://10.170.121.125'
            Mashery_dir='prdurlMashery'
        return (BW_dir,Mashery_dir)
