import scrapy
import codecs


class QuotesSpider(scrapy.Spider):
    name = "datos_equipos"

    def start_requests(self):
        
        archivo = open("data/urls_equipos.csv", "r") #Lee la direccion principal y lo guarda en 'archivo'.
        archivo = archivo.readlines()
        archivo = [a.strip() for a in archivo]
        for url in archivo:
            yield scrapy.Request(url=url, callback=self.parse)

    

    def parse(self, response):
        
        with codecs.open("data/datos_equipos.csv", 'a', encoding='utf-8') as f: #Response principal
            pagina= response.xpath('//div[@class="col-md-6"]')
            div = pagina.xpath('article/div/div/ul/li/article/div/div/div')
            for x in div:
                lista = x.xpath('p')
                br = lista.xpath('strong')

                if len(br) > 0:
                    nombre = br[0].xpath('text()').extract()[0].strip('\n')
                    categoria = br[1].xpath('text()').extract()[0].strip('\n')
                    fundacion = br[2].xpath('text()').extract()[0].strip('\n')
                    direccion = br[3].xpath('text()').extract()[0].strip('. ')
                    telefono = br[4].xpath('text()').extract()[0].strip(' ')
                    fax = br[5].xpath('text()').extract()[0].strip('\n')
                    sitio = br[6].xpath('a/text()').extract()[0].strip('\n')
                    email = br[7].xpath('a/text()').extract()[0].strip('\n')
                    
                    responsive  = div[0].xpath('div[@class="table-responsive"]')#PERMITE OBTENER EL PRIMER DIV
                    tablas = responsive.xpath('table')
                    
                    if categoria == 'PRIMERA - A': 
                        if len(tablas) == 3:
                            tb = tablas[0].xpath('tbody')#OBTIENE TODOS LOS TBODY DE LA PRIMERA TABLA
                            td = tb[0].xpath('tr/td') #SACA TODO LOS TD QUE ESTAN DENTRO DEL TBDODY
                            if td[0].xpath('text()').extract()[0] == 'Campeonatos Serie "A"':
                                campeonatos = td[1].xpath('text()').extract()[0][:2]
                                tb2 = tablas[1].xpath('tbody') #saca el tbdody de la siguiente tabla
                                td2 = tb2[0].xpath('tr/td')
                                presidente = td2[1].xpath('text()').extract()[0]
                                #f.write(u"%s|%s\n" %(presidente,campeonatos))
                            
                            elif td[0].xpath('text()').extract()[0] == 'Ganador Serie "B"':
                                tb2 = tablas[1].xpath('tbody')
                                td2 = tb2.xpath('tr/td') 
                                presidente = td2[1].xpath('text()').extract()[0]
                                campeonatos = 0
                                #f.write(u"%s|%s\n" %(presidente,campeonatos))
                            
                            else:
                                tb2 = tablas[1].xpath('tbody')
                                td2 = tb2[0].xpath('tr/td')
                                presidente = td2[1].xpath('text()').extract()[0]
                                campeonatos = 0
                                
                        else:
                            tb = tablas[0].xpath('tbody')
                            td = tb[0].xpath('tr/td')
                            campeonatos = 0
                            presidente = td[1].xpath('text()').extract()[0]
                            #f.write(u"%s|%s\n" %(presidente,campeonatos))

                    else:
                        if len(tablas) == 3:
                            tb = tablas[0].xpath('tbody')
                            td = tb[0].xpath('tr/td')
                            contador = 0
                            for l in td:
                                if td[contador].xpath('text()').extract()[0] == 'Ganador Serie "B"':
                                    campeonatos = td[contador + 1].xpath('text()').extract()[0][:2]
                                    tb2 = tablas[1].xpath('tbody')
                                    td2 = tb2[0].xpath('tr/td')
                                    presidente = td2[1].xpath('text()').extract()[0]
                                    break
                                    #f.write(u"%s|%s\n" %(presidente,campeonatos)) 
                                else:
                                    tb2 = tablas[1].xpath('tbody')
                                    td2 = tb2[0].xpath('tr/td')
                                    presidente = td2[1].xpath('text()').extract()[0]
                                    campeonatos = 0

                                contador += 1
                        else:
                            tb = tablas[0].xpath('tbody')
                            td = tb[0].xpath('tr/td')
                            campeonatos = 0
                            presidente = td[1].xpath('text()').extract()[0]
                    
                    responsive2 = div[1].xpath('div[@class="table-responsive"]') #SACA EL SEGUNDO DIV 
                    tablas2 = responsive2.xpath('table') #OBTIENE TODAS LAS TABLAS
                    
                    datos_estadio = tablas2[1].xpath('thead/tr') #SACA LOS TR DE LA PRIMERA TABLA
                    nombre_estadio = datos_estadio.xpath('th/text()').extract()[0]
                    datos_estadio = tablas2[1].xpath('tbody/tr') #SACA LOS TR DE LA SEGUNDA TABLA
                    capacidad = datos_estadio[5].xpath('td/strong/text()').extract()[0]
                            
            f.write(u"%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s\n" %(nombre,categoria,presidente,fundacion,telefono,fax,sitio,email,campeonatos,nombre_estadio,capacidad,direccion))   
                
        f.close()
    
