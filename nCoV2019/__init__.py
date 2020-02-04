import requests,json
from pandas import DataFrame as DF
class qq_source:
    
    def __init__(self):
        self.data_url = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5'
        x = requests.get(self.data_url).json()
        data = json.loads(x['data'])
        header = ['time','confirm','suspect','dead','heal','confirm_add','suspect_add','dead_add','heal_add']
        self.chinaDayList = DF([ list(i.values()) for i in data['chinaDayList'] ],columns=header[:5])
        self.chinaDayADD = DF([ list(i.values()) for i in data['chinaDayAddList'] ],columns=header[:5])
        print(f'截止 {data["lastUpdateTime"]}; 2019nCoV 已蔓延 {len(data["areaTree"])} 个国家/地区')
        print(f'中国累计 {data["chinaTotal"]["confirm"]} 例确诊，自昨日00:00新增{data["chinaAdd"]["confirm"]}')
    
        # 各个地区数据
        areaTree = data['areaTree']
        self.area_dict = {} #记录全部地区
        self.total_rec = [self._detail_area(i) for i in areaTree] #解析全部记录
        self.all_area = set(self.area_dict.keys()) # 所有的地名
        self.global_area = DF(self._country(areaTree),columns=['city'] + header[1:]) # 全球感染情况
        self.china = DF(self._country(areaTree[0]['children']),columns=['city'] + header[1:]) # 国内感染情况
        
    def _city_row(self,city):
        name = city['name']
        today = list(city['today'].values())
        total = list(city['total'].values())
        return([[name] + total + today])
    
    def _detail_area(self,area):
        city_row = self._city_row(area)
        name = city_row[0][0]
        # 如果地区还能细分
        sp = 'children' in area.keys()
        if sp:
            for city in area['children']:
                city_row = city_row + self._detail_area(city)
        header = ['city','confirm','suspect','dead','heal','confirm_add','suspect_add','dead_add','heal_add']
        df = DF(city_row,columns=header)
        self.area_dict[name] = df
        return(city_row)
    
    def _country(self,area,opt=0):
        city_rows = []
        for country in area:
            city_row = self._city_row(country)
            city_rows += city_row
        return(city_rows)

    def get(self,area_name):
        try:
            return(self.area_dict[area_name])
        except KeyError as e:
            print(f'{e} 尚无 2019nCoV感染记录/未收录')
            return None
    def search(self,area_name):
        return [m for m in self.all_area if area_name in m ]
