# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class RetalhosPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        
        # Adaptando o preço para o caso de salvamento num arquivo,
        # pois o símbolo de libra esterlina (£) não pode ser salvo normalmente.
        # Sei que não é a melhor prática, e que seria melhor transformar em float,
        # mas fiz assim por propósitos de visualização agradável
        value = adapter.get('Price')

        if value:
            adapter['Price'] = value.replace('£', 'GBP ')

        return item
