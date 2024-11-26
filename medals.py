#!/usr/bin/env python
# coding: utf-8

# In[1]:


import csv
import json
class CountryMedals:
    
    def __init__(self,name,gold,silver,bronze):
        self.name= name
        self.gold= gold
        self.silver= silver
        self.bronze= bronze
        
    def to_json(self):
        total= self.gold+self.silver+self.bronze
        return {'name': self.name,'gold':self.gold,'silver':self.silver,'bronze':self.bronze,'total':total}
    
    def get_medals(self,medal_type):
        if medal_type=='gold':
            return self.gold
        
        elif medal_type=='silver':
            return self.silver
        
        elif medal_type=='bronze':
            return self.bronze
        
        elif medal_type=='total':
            return self.gold+self.silver+self.bronze
        
        else:
            return None
        
    def print_summary(self):
        total= self.gold+self.silver+self.bronze
        print('{} received {} medals in total; {} gold, {} silver, and {} bronze'.format(self.name,total,self.gold,self.silver,self.bronze))
        
    def compare(self, country_2):
        total1 = self.gold+self.silver+self.bronze
        total2 = country_2.get_medals('total')
        
        print('Medals comparison between {} and {}:'.format(self.name,country_2.name))
        
        #For Gold Medal
        
        if self.gold==country_2.gold:
            print('-Both {} and {} received {} gold medal(s).'.format(self.name,country_2.name,self.gold))
            
        elif self.gold>country_2.gold:
            print('-{} received {} gold medal(s), {} more than {}, which received {}.'.format(self.name,self.gold,self.gold-country_2.gold,country_2.name,country_2.gold))
        
        else:
            print('-{} received {} gold medal(s), {} fewer than {}, which received {}.'.format(self.name,self.gold,country_2.gold-self.gold,country_2.name,country_2.gold))
            
            
        #For Silver Medal
        
        if self.silver==country_2.silver:
            print('-Both {} and {} received {} silver medal(s).'.format(self.name,country_2.name,self.silver))
            
        elif self.silver>country_2.silver:
            print('-{} received {} silver medal(s), {} more than {}, which received {}.'.format(self.name,self.silver,self.silver-country_2.silver,country_2.name,country_2.silver))
        
        else:
            print('-{} received {} silver medal(s), {} fewer than {}, which received {}.'.format(self.name,self.silver,country_2.silver-self.silver,country_2.name,country_2.silver))
            
            
        #For Bronze Medal
            
        if self.bronze==country_2.bronze:
            print('-Both {} and {} received {} bronze medal(s).'.format(self.name,country_2.name,self.bronze))
            
        elif self.bronze>country_2.bronze:
            print('-{} received {} bronze medal(s), {} more than {}, which received {}.'.format(self.name,self.bronze,self.bronze-country_2.bronze,country_2.name,country_2.bronze))
        
        else:
            print('-{} received {} bronze medal(s), {} fewer than {}, which received {}.'.format(self.name,self.bronze,country_2.bronze-self.bronze,country_2.name,country_2.bronze))
            
        #For Total
        
        if total1==total2:
            print('-Overall, {} and {}, both received {} total medal(s) each.'.format(self.name,country_2.name,total1))
            
        elif total1>total2:
            print('-Overall, {} received {} medal(s), {} more than {}, which received {} medal(s).'.format(self.name,total1,total1-total2,country_2.name,total2))
        
        else:
            print('-Overall, {} received {} medal(s), {} fewer than {}, which received {} medal(s).'.format(self.name,total1,total2-total1,country_2.name,total2))
            
            
    def get_sorted_list_of_country_names(countries):
        countries_string= ','.join(sorted(countries.keys()))
        print(countries_string)
            
    def sort_countries_by_medal_type_ascending(countries,type_of_medal):
        return sorted(countries.values(), key=lambda country: country.get_medals(type_of_medal))
        
    def sort_countries_by_medal_type_descending(countries,type_of_medal):
        return sorted(countries.values(), key=lambda country: country.get_medals(type_of_medal), reverse=True)
        
    def read_positive_integer():
            
        threshold_val=int(input("Enter the threshold (a positive integer):"))
        if(threshold_val>0):
            return threshold_val
            
        else:
            print("Please enter a positive integer")
            return CountryMedals.read_positive_integer()
            
    def read_country_name(countries):
            
        country_name=input("Insert a country name('q for quit'): ")
        if country_name in countries:
            return country_name
        elif country_name=='q':
            return 'q'
        else:
            print("Please enter a valid country ")
            print("Available countries are as follows:",CountryMedals.get_sorted_list_of_country_names(countries))
            return CountryMedals.read_country_name(countries)
            
    def read_medal_type():
            
        medal_type=input("Insert a medal type (choose among 'gold','silver','bronze' or 'total'):")
        list1=['gold','silver','bronze','total']
        if medal_type in list1:
            return medal_type
            
        else:
            print('Please enter a valid medal type')
            return CountryMedals.read_medal_type()
            
    def more_medals_than_threshold(countries,threshold,medal_type):
        countries_with_more_medals=[]
        for country in countries.values():
            if country.get_medals(medal_type)>threshold:
                countries_with_more_medals.append(country)
                    
        sorted_countries=sorted(countries_with_more_medals, key=lambda country: country.get_medals(medal_type),reverse=True)
            
        return sorted_countries
        
    def fewer_medals_than_threshold(countries, threshold,medal_type):
            
        countries_with_fewer_medals=[]
        for country in countries.values():
                if country.get_medals(medal_type)<threshold:
                    countries_with_fewer_medals.append(country)
                        
        sorted_countries=sorted(countries_with_fewer_medals, key=lambda country: country.get_medals(medal_type))
        return sorted_countries
        
    def main():
        countries={}
            
        with open(r'/Users/niharika21/Downloads/medals.csv',encoding='latin1') as csvfile:
            reader=csv.reader(csvfile)
            try:
                next(reader)
                for line in reader:
                    rank,name,gold,silver,bronze,total,rank_by_total=line
                    country_instance=CountryMedals(name,int(gold),int(silver),int(bronze))
                    countries[name]=country_instance
            except StopIteration:
                print("No data found in the CSV file.")
                    
            
        stop= False
        while not stop:
            command=input('Insert a command (Type "h" for help):').lower()
                
            if command=='h':
                print("\nList of commands:\n- (H)elp shows the list of comments;\n- (L)ist shows the list of countries present in the dataset;\n- (S)ummary prints out a summary of the medals won by a single country;\n- (C)ompare allows for a comparison of the medals won by two countries;\n- (M)ore, given a medal type, lists all the countries that received more medals than a threshold;\n- (F)ewer, given a medal type, lists all the countries that received fewer medals than a threshold;\n- (E)xport, save the medals table as '.json' file;\n- (Q)uit")
                    
            elif command=='l':
                print("The dataset contains 98 countries:")
                country_name=CountryMedals.get_sorted_list_of_country_names(countries)
                    
            elif command=='s':
                country_name=CountryMedals.read_country_name(countries)
                if country_name=='q':
                    return
                    
                else:
                    country=countries[country_name]
                    country.print_summary()
                        
            elif command=='c':
                print("Compare two countries")
                country_name= input("Insert a country name ('q' for quit): ")
                if country_name=='q':
                    return
                    
                else:
                    print("Insert the name of the country you want to compare against (country_name)")
                    country_name2= input("Insert a country name ('q' for quit): ")
                    print("Medals comparison between {country_name} and {country_name2}")
                    country1=countries[country_name]
                    country2=countries[country_name2]
                    country1.compare(country2)
                        
            elif command=='m':
                print("Given a medal type, list all the countries that received more medals than a threshold:")
                medal_type=CountryMedals.read_medal_type()
                threshold=CountryMedals.read_positive_integer()
                countries_with_more_medals=CountryMedals.more_medals_than_threshold(countries,threshold,medal_type)
                    
                if len(countries_with_more_medals)==0:
                    print(f"No countries received more than {threshold}")
                        
                else:
                    print(f"Countries that received more than {threshold} '{medal_type}' medals:")
                    print()
                        
                    for country in countries_with_more_medals:
                        print(f" - {country.name} received {country.get_medals(medal_type)}")
                            
                            
            elif command=="f":
                print("Given a medal type, list all the countries that received fewer medals than a threshold:")
                medal_type=CountryMedals.read_medal_type()
                threshold=CountryMedals.read_positive_integer()
                    
                print(f"Insert a medal type( choose among 'gold', 'silver', 'bronze' or 'total'): {medal_type}")
                print(f"Enter the threshold (a positive integer): {threshold}")
                    
                countries_with_fewer_medals=CountryMedals.fewer_medals_than_threshold(countries,threshold,medal_type)
                    
                if len(countries_with_fewer_medals)==0:
                    print(f"No countries received less than {threshold}")
                        
                else:
                    print(f"Countries that received fewer than {threshold} '{medal_type}' medals:")
                    print()
                        
                    for country in countries_with_fewer_medals:
                        print(f" - {country.name} received {country.get_medals(medal_type)}")
                            
                            
            elif command=='e':
                export_data={country_instance.name: country_instance.to_json() for country_instance in countries.values()}
                file_name=input("Enter the file name (.json):")
                
                with open(f"{file_name}.json",'w') as json_file:
                    json.dump(export_data,json_file,indent=4)
                    print(f"File {file_name} correctly saved")
                    
                output_data = {}    #This will show an example of a portion of the exported JSON file including all the medals
                for country in countries.values():
                    output_data[country.name] = {"name":country.name,"gold": country.gold,"silver": country.silver,"bronze": country.bronze,"total": country.gold + country.silver + country.bronze}
                    print(output_data[country.name])
                    
                        
            elif command=='q':
                print("Goodbye!")
                break
                    
            else:
                print('Please enter proper command')
                            
 


# In[ ]:



if __name__ == "__main__":
    CountryMedals.main()                          
    


# In[ ]:




