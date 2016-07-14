Search.setIndex({envversion:50,filenames:["api","description","index","installation","modules","notes","overview","running","site_analytics","site_analytics.admin","site_analytics.apps","site_analytics.filters","site_analytics.manage","site_analytics.managers","site_analytics.migrations","site_analytics.migrations.0001_initial","site_analytics.models","site_analytics.serializers","site_analytics.settings","site_analytics.settings_local","site_analytics.tests","site_analytics.transforms","site_analytics.urls","site_analytics.views","site_analytics.wsgi","ui"],objects:{"":{site_analytics:[8,0,0,"-"]},"site_analytics.admin":{RequestAdmin:[9,1,1,""]},"site_analytics.admin.RequestAdmin":{Meta:[9,1,1,""],media:[9,2,1,""]},"site_analytics.admin.RequestAdmin.Meta":{model:[9,2,1,""]},"site_analytics.apps":{SiteAnalyticsAppConfig:[10,1,1,""]},"site_analytics.apps.SiteAnalyticsAppConfig":{name:[10,2,1,""],verbose_name:[10,2,1,""]},"site_analytics.filters":{IsoDateTimeFromToRangeFilter:[11,1,1,""],IsoDateTimeRangeField:[11,1,1,""],RequestFilter:[11,1,1,""]},"site_analytics.filters.IsoDateTimeFromToRangeFilter":{field_class:[11,2,1,""]},"site_analytics.filters.RequestFilter":{Meta:[11,1,1,""],base_filters:[11,2,1,""],declared_filters:[11,2,1,""],qs:[11,2,1,""],strict:[11,2,1,""]},"site_analytics.filters.RequestFilter.Meta":{fields:[11,2,1,""],model:[11,2,1,""]},"site_analytics.manage":{main:[12,3,1,""]},"site_analytics.managers":{RequestManager:[13,1,1,""],quote_ident:[13,3,1,""]},"site_analytics.managers.RequestManager":{get_user_count:[13,4,1,""],get_user_counts:[13,4,1,""],get_user_field_expr:[13,4,1,""]},"site_analytics.migrations":{"0001_initial":[15,0,0,"-"]},"site_analytics.migrations.0001_initial":{Migration:[15,1,1,""]},"site_analytics.migrations.0001_initial.Migration":{dependencies:[15,2,1,""],initial:[15,2,1,""],operations:[15,2,1,""]},"site_analytics.models":{Request:[16,1,1,""]},"site_analytics.models.Request":{DoesNotExist:[16,5,1,""],MultipleObjectsReturned:[16,5,1,""],clean:[16,4,1,""],get_data_column:[16,6,1,""],get_next_by_timestamp:[16,4,1,""],get_previous_by_timestamp:[16,4,1,""],objects:[16,2,1,""],set_geoip_data:[16,4,1,""]},"site_analytics.serializers":{RequestSerializer:[17,1,1,""]},"site_analytics.serializers.RequestSerializer":{Meta:[17,1,1,""],STATIC_FIELDS:[17,2,1,""],to_internal_value:[17,4,1,""],to_representation:[17,4,1,""]},"site_analytics.serializers.RequestSerializer.Meta":{model:[17,2,1,""]},"site_analytics.tests":{BaseAPITestCase:[20,1,1,""],RequestAPITestCase:[20,1,1,""],RequestModelTestCase:[20,1,1,""],RequestQueryTestCase:[20,1,1,""],VersionAPITestCase:[20,1,1,""]},"site_analytics.tests.BaseAPITestCase":{assertRecentTimestamp:[20,4,1,""],assertTimestamp:[20,4,1,""],get_url_base:[20,7,1,""]},"site_analytics.tests.RequestAPITestCase":{test_get:[20,4,1,""],test_post:[20,4,1,""],test_post_invalid_missing_url:[20,4,1,""],test_post_invalid_url:[20,4,1,""],test_post_with_data:[20,4,1,""]},"site_analytics.tests.RequestModelTestCase":{create_request:[20,4,1,""],test_get_user_count:[20,4,1,""],test_get_user_counts:[20,4,1,""],test_set_geoip_data:[20,4,1,""],test_set_geoip_data_do_not_overwrite:[20,4,1,""],test_set_geoip_data_no_ip_address:[20,4,1,""],test_set_geoip_data_no_user:[20,4,1,""],test_set_geoip_data_private_address:[20,4,1,""],test_str:[20,4,1,""]},"site_analytics.tests.RequestQueryTestCase":{addresses:[20,2,1,""],path:[20,2,1,""],request_data:[20,2,1,""],setUpTestData:[20,6,1,""],sites:[20,2,1,""],test_filter_ip_address:[20,4,1,""],test_filter_site:[20,4,1,""],test_filter_state:[20,4,1,""],test_filter_timestamp:[20,4,1,""],test_filter_timestamp_invalid_format:[20,4,1,""],test_filter_timestamp_multiple:[20,4,1,""],test_filter_timestamp_not_before:[20,4,1,""],test_filter_timestamp_range:[20,4,1,""],test_filter_url:[20,4,1,""],test_filter_username:[20,4,1,""],test_filter_username_and_timestamp_not_after:[20,4,1,""],test_pagination:[20,4,1,""],users:[20,2,1,""]},"site_analytics.tests.VersionAPITestCase":{test_get:[20,4,1,""]},"site_analytics.transforms":{UrlSiteTransform:[21,1,1,""]},"site_analytics.transforms.UrlSiteTransform":{"function":[21,2,1,""],lookup_name:[21,2,1,""]},"site_analytics.views":{FilterView:[23,1,1,""],RequestViewSet:[23,1,1,""],SummaryView:[23,1,1,""],VersionViewSet:[23,1,1,""]},"site_analytics.views.FilterView":{get:[23,4,1,""],renderer_classes:[23,2,1,""],template_name:[23,2,1,""]},"site_analytics.views.RequestViewSet":{filter_class:[23,2,1,""],queryset:[23,2,1,""],serializer_class:[23,2,1,""],suffix:[23,2,1,""]},"site_analytics.views.SummaryView":{get:[23,4,1,""],renderer_classes:[23,2,1,""],template_name:[23,2,1,""]},"site_analytics.views.VersionViewSet":{list:[23,4,1,""],suffix:[23,2,1,""]},site_analytics:{admin:[9,0,0,"-"],apps:[10,0,0,"-"],filters:[11,0,0,"-"],manage:[12,0,0,"-"],managers:[13,0,0,"-"],migrations:[14,0,0,"-"],models:[16,0,0,"-"],serializers:[17,0,0,"-"],settings:[18,0,0,"-"],settings_local:[19,0,0,"-"],tests:[20,0,0,"-"],transforms:[21,0,0,"-"],urls:[22,0,0,"-"],views:[23,0,0,"-"],wsgi:[24,0,0,"-"]}},objnames:{"0":["py","module","Python module"],"1":["py","class","Python class"],"2":["py","attribute","Python attribute"],"3":["py","function","Python function"],"4":["py","method","Python method"],"5":["py","exception","Python exception"],"6":["py","classmethod","Python class method"],"7":["py","staticmethod","Python static method"]},objtypes:{"0":"py:module","1":"py:class","2":"py:attribute","3":"py:function","4":"py:method","5":"py:exception","6":"py:classmethod","7":"py:staticmethod"},terms:{"000000z":20,"0001_initi":[],"01t00":20,"01t04":20,"01t05":20,"01t06":20,"02t00":20,"03t02":20,"03t22":20,"100000z":20,"300000z":20,"500000z":20,"600000z":20,"700000z":20,"800000z":20,"826391z":20,"break":5,"case":11,"class":[9,10,11,13,15,16,17,20,21,23],"default":[0,16,25],"export":[7,25],"function":[15,21],"import":3,"int":13,"null":[0,3,15],"return":[0,13,15,16,23],"static":[7,20],"true":15,abbrevi:11,about:1,absolut:0,accc4cf8:3,accept:25,access:25,accord:5,action:11,activ:[3,7,25],add:[3,5,7],addit:[0,25],address:[5,11,16,20],admin:[],admin_sit:9,after:11,alia:[9,11,17,23],all:[0,1,7],allow:6,along:0,also:[0,25],analyt:1,ani:[16,25],any:0,apitestcas:20,apiview:23,app:[],app_label:15,app_modul:10,app_nam:10,appconfig:10,applicat:10,apt:3,arg:[11,16,23],argument:11,arrai:0,asc:3,assertrecenttimestamp:20,asserttimestamp:20,author:11,autofield:15,automat:23,base:[9,10,11,13,15,16,17,20,21,23],base_filt:11,baseapitestcas:20,befor:11,begin:7,best:[1,3],bill:20,bin:3,bob:20,brows:25,browsabl:[],button:25,can:[1,3,11,16,25],cart:20,categori:25,certain:25,chang:3,charact:11,charfilt:11,classmethod:[16,20],clean:16,click:25,client:[6,16],clone:3,code:25,collect:[7,16,23,25],collectstat:7,column:16,com:3,command:7,comment:25,compat:5,complet:25,config:[10,24],configur:[9,10,22],contain:[0,25],content:2,contrib:[9,15],control:7,core:16,count:[0,13,25],creat:3,create:15,create_request:20,createdb:3,createmodel:15,createmodelmixin:23,createsuperus:25,createus:3,criteria:25,crude:5,current:[0,16],data:[0,1,5,11,15,16,17,20,25],databas:[],date:[0,11,25],datetim:11,datetimefield:15,datetimefromtorangefilt:11,db_tabl:15,dbms:3,deb:3,declared_filt:11,depend:[7,15],desir:25,detail:[0,16],determin:16,dev:3,develop:3,direct:25,directori:3,disabl:25,distinct:11,django:[9,10,13,15,16,18,20,21,25],django_filt:11,docstr:0,document:1,doesnotexist:16,drop:15,each:[0,11],easier:16,echo:3,element:0,empti:17,enabl:25,endpoint:25,ensure:7,enter:25,entiti:[0,23],environ:[],etc:[3,7],exact:11,exampl:3,except:[16,25],exclud:11,execut:7,express:[13,21],extens:13,extra:21,fals:11,featur:23,field:[0,5,11,13,15,16,17,25],field_class:11,file:7,fill:16,filter:[0,1,5],filter_class:23,filterset:11,filterview:23,first:0,focu:13,follow:0,form:25,format:[11,25],framework:[11,25],from:[3,11,15,25],further:25,gain:1,genericviewset:23,geoip:[5,11,16,20],get_data_column:16,get_next_by_timestamp:16,get_previous_by_timestamp:16,get_url_bas:20,get_user_count:13,get_user_field_expr:13,gin:15,git:3,github:[1,3],given:[0,13,16],gnuworldman:3,goe:16,have:[1,11],help:7,host1:20,host2:20,host3:20,host4:20,host:[1,25],html:[5,20,23,25],http:[3,20],hyperlinkedmodelseri:17,identifi:[11,13,16],implement:[5,23],includ:0,inclus:25,incom:16,index:[2,15,20],initi:[7,15],input:[15,25],insight:1,instal:[3,7],install:3,installat:[],instanc:17,interact:25,interfac:5,interpret:[],ip_address:[11,16,20],iso:[11,25],isodatetimefromtorangefilt:11,isodatetimerangefield:11,issu:1,jack:20,jill:20,jsonb:[0,15],jsonfield:15,kei:[3,13],known:16,kwarg:[11,16,17,23],label:11,last:0,least:0,let:16,librari:3,like:25,list:[3,23,25],listmodelmixin:23,locat:16,login:[20,25],look:16,lookup:21,lookup_expr:11,lookup_nam:21,lsb_releas:3,made:[0,11,16],mai:[16,25],main:[3,12],make:25,manag:[],map:13,match:[0,25],media:[3,9],meta:[9,11,17],method:[0,23],methodnam:20,midget:20,might:7,migrat:[],mixin:23,model:0,modeladmin:9,modul:[],more:25,morearg:16,morekwarg:16,multipleobjectsreturn:16,must:[7,11,25],name:[10,11,13,15,16,20],nas:15,nbegin:15,necessari:7,need:3,nend:15,net:20,next:[0,3],nimmutable:15,nlanguage:15,noinput:7,none:[11,17,23],normal:23,note:[],now:5,nreturns:15,number:[0,13,23,25],object:[0,9,11,13,16,17,25],objectdoesnotexist:16,old:5,onli:23,oper:15,option:[9,15,25],order:20,ordereddict:[11,13],org:3,origin:16,other:0,overrid:11,overview:[],overwrit:16,packag:[],page:0,pagin:0,paramet:[0,11,13,16],particular:16,path:[7,20,25],payload:0,persist:[0,1,6,16,25],pertin:[0,1],pgdg:3,pip:7,plpgsql:15,point:3,popul:16,port:[7,25],postgr:[3,15],postgresql:3,prefix:11,prepend:7,prerequisit:[],previou:[0,5],print:3,probabl:3,process:[1,16],produc:11,project:[3,7,9,10,11,13,15,16,17,18,20,21,22,23,24],project_root:[7,25],prompt:7,provid:[16,25],psycopg2:13,pub:3,pull:13,put:25,python3:3,python:[3,7],pythonpath:[7,25],queri:[0,6,16,25],queryset:[11,23],quot:13,quote_id:13,raise:11,rang:11,rangefield:11,rather:25,realli:3,recommend:[3,7],regard:0,region:[5,11,16,20],relat:[0,1],releas:[],remaind:16,render:23,renderer_class:23,replac:13,replace:15,repo:3,request_data:20,request_data_index:15,request_url_sit:15,requestadmin:9,requestapitestcas:20,requestfilt:[0,11,16,23],requestmanag:[13,16],requestmodeltestcas:20,requestquerytestcas:20,requestseri:[17,23],requestviewset:[17,23],requir:[0,7,11,16,25],resid:11,resourc:[0,20],respect:16,respons:20,rest:[11,25],rest_framework:[17,20,23,25],restful:1,result:[0,3],retriev:[0,1],retrievemodelmixin:23,role:3,rout:23,run:3,runserv:7,runsql:15,runtest:20,same:[0,25],save:16,scheme:[11,25],script:3,search:2,second:20,section:3,see:[0,7,16,25],self:[0,17],sent:16,serial:[],serializer_class:23,server:3,servic:[0,1],set:[],set_geoip_data:16,settings_loc:[],setup:3,setuptestdata:20,shell:7,should:16,site:1,site_analyt:3,siteanalyticsappconfig:10,size:0,some:25,sourc:1,special:16,specifi:[11,16],sql:13,src:[7,25],stabl:13,start:[],state:[5,11,16],static_fields:17,store:[0,16],str:13,strict:11,string:[0,23],stuff:20,submit:25,submodul:[],subpackag:[],substring:15,sudo:[3,7],sue:20,suffix:23,summari:5,summaryview:23,superus:25,support:0,sure:25,system:[16,25],tee:3,template_nam:23,templatehtmlrender:23,terri:20,test:5,test_filter_ip_address:20,test_filter_sit:20,test_filter_st:20,test_filter_timestamp:20,test_filter_timestamp_invalid_format:20,test_filter_timestamp_multipl:20,test_filter_timestamp_not_befor:20,test_filter_timestamp_rang:20,test_filter_url:20,test_filter_usernam:20,test_filter_username_and_timestamp_not_aft:20,test_get:20,test_get_user_count:20,test_pagin:20,test_post:20,test_post_invalid_missing_url:20,test_post_invalid_url:20,test_post_with_data:20,test_set_geoip_data:20,test_set_geoip_data_do_not_overwrit:20,test_set_geoip_data_no_ip_address:20,test_set_geoip_data_no_us:20,test_set_geoip_data_private_address:20,test_str:20,testcas:20,than:25,thei:25,thi:[0,1,3,5,6,11,13,16,25],thing:20,three:16,time:[0,11,16,25],timestamp:[0,11,15,16,17,20,25],timestamp_0:11,timestamp_1:11,to_internal_valu:17,to_represent:17,top:[13,25],total:[0,25],transform:[],two:[11,25],txt:7,type:13,ubuntu:3,under:25,uniqu:13,unit:5,updat:3,upper:11,url:0,url_sit:[15,21],urlfield:15,urlsitetransform:21,use:[16,25],user:[0,3,5],user_field:13,usernam:[11,16],using:15,validationerror:11,valu:[11,13,16,20,25],varchar:15,venv:3,verbose_nam:10,version_info:3,versionapitestcas:20,versionviewset:23,via:[],view:[],viewset:23,virtual:[],virtualenv:3,wai:[1,16],want:[3,7],web:1,were:11,wget:3,when:[0,13],where:1,which:[0,16,23],whose:16,widget:[11,20],within:[11,13],without:7,wsgi:[],www:3,yet:5,you:[3,7]},titles:["Request information","&lt;no title&gt;","Site Analytics documentation","Installation","site_analytics","Release Notes","Overview","Running","site_analytics package","site_analytics.admin module","site_analytics.apps module","site_analytics.filters module","site_analytics.manage module","site_analytics.managers module","site_analytics.migrations package","site_analytics.migrations.0001_initial module","site_analytics.models module","site_analytics.serializers module","site_analytics.settings module","site_analytics.settings_local module","site_analytics.tests module","site_analytics.transforms module","site_analytics.urls module","site_analytics.views module","site_analytics.wsgi module","User Interface"],titleterms:{"0001_initi":15,admin:[9,25],analyt:2,api:[0,25],app:10,browsabl:25,call:0,creat:25,databas:3,document:2,environ:3,filter:[11,25],get:0,indice:2,inform:0,installat:3,interfac:25,interpret:3,manag:[12,13],migrat:[14,15],model:16,modul:[9,10,11,12,13,15,16,17,18,19,20,21,22,23,24],note:5,overview:6,packag:[8,14],page:25,post:0,prerequisit:7,releas:5,request:0,run:7,serial:17,servic:7,set:18,settings_loc:19,site:2,site_analyt:[4,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24],sourc:3,start:7,submodul:[8,14],subpackag:8,summari:25,tabl:2,test:20,transform:21,url:22,user:25,version:[0,5],via:3,view:23,virtual:3,wsgi:24}})