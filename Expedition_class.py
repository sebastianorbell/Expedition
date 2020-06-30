import numpy as np
import matplotlib.pyplot as plt

class Expedition():
    def __init__(self,continent,countries,season,loop=False):
        self.continent = continent
        self.countries = countries
        self.loop = loop
        self.season = season
        
    def create_sections_dict(self,names,distances,direct_times=None):
        self.names = names
        self.property_names = ['Distance','Direct time']
        self.properties = [distances,direct_times]
        self.sections = self.create(names,self.property_names,self.properties)

    def create(self,names,property_names,properties):
        s_dict = []
        for index,name in enumerate(names):
            s_properties = []
            for prop in properties:
                s_properties.append(prop[index])
                    
            s_dict.append(self.mdict(property_names,s_properties))
        sections = self.mdict(names,s_dict)
        return sections
                
    def mdict(self,names,properties):
        a_dict = {}
        for index,name in enumerate(names):
            a_dict[str(name)] = properties[index]
        return a_dict
    
    def plot_property(self,prop):
        y = []
        for name in self.names:
            y.append(self.sections[name][prop])
        
                
        y_pos = np.arange(len(self.names))
        
        plt.bar(y_pos, y, align='center', alpha=0.5)
        plt.xticks(y_pos, self.names)
        plt.xlabel('Section')
        plt.ylabel(prop)
        plt.title('Plot of '+prop)
        
        plt.show()

    def plot_properies(self,props):
        
        ys = []
        for index,prop in enumerate(props):
            y =[]
            for name in self.names:
                y.append(self.sections[name][prop])
            ys.append(y)
            
        fig, ax = plt.subplots()
        name_pos = np.arange(len(names))
        bar_width = 1/(len(props)+1)
        opacity = 0.8
        
        for index, prop in enumerate(props):
            plt.bar(name_pos+index*bar_width, ys[index], bar_width,
        alpha=opacity,label = prop)
        
        plt.xlabel('Section')
        plt.ylabel('Property Value')
        plt.title('Multiple property values')
        plt.xticks(name_pos+bar_width*0.5, self.names)
        plt.legend()
        
        plt.tight_layout()
        plt.show()

class Hike(Expedition):
	pass

class Bike(Expedition):
	pass

class Ultra(Expedition):
	pass

class Kayak(Expedition):
	pass

hike = Hike('Europe','England','Summer')
names = ['a','b','c']
distances = [100,200,300]
times = [6,7,8]

hike.create_sections_dict(names,distances,direct_times=times)
print(hike.sections['a']['Distance'])
hike.plot_property('Distance')
hike.plot_property('Direct time')
hike.plot_properies(['Direct time','Distance'])