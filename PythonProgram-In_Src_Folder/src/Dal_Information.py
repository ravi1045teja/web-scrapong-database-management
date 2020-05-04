'''
Created on Sep. 24, 2019

@author: ravitejakase
'''
import requests
from bs4 import BeautifulSoup

underGraduatePrograms=[]
graduatePrograms=[]
professionalPrograms=[]
programs_list=[]
faculty_list=[]
empFrstName=[]
empScndName=[]

def buildTree(rootTag,subEle1,subEle2,subEle3,lst1,lst2):
    
    a='<'+rootTag+'>'
    for i in range(len(lst1)) :
        a+='<'+subEle1+'>'
        a+='<'+subEle2+'>'+lst1[i]+'</'+subEle2+'>'
        a+='<'+subEle3+'>'+lst2[i]+'</'+subEle3+'>'
        a+='</'+subEle1+'>' 
        
    a+='</'+rootTag+'>'
    return a

def buildTree1(rootTag,subEle1,subEle2,subEle3,subEle4,lst1,lst2,pid):
    
    a='<'+rootTag+'>'
    for i in range(len(lst1)) :
        a+='<'+subEle1+'>'
        a+='<'+subEle2+'>'+lst1[i]+'</'+subEle2+'>'
        a+='<'+subEle3+'>'+lst2[i]+'</'+subEle3+'>'
        a+='<'+subEle4+'>'+pid+'</'+subEle4+'>'
        a+='</'+subEle1+'>' 
        
    a+='</'+rootTag+'>'
    return a

def buildExtension(str1,subEle1,subEle2,subEle3,subEle4,lst1,lst2,l,pid):
    c=str1.rfind('</')
    d=''
    for i in range(l,len(lst1)):
        d+='<'+subEle1+'>'
        d+='<'+subEle2+'>'+lst1[i]+'</'+subEle2+'>'
        d+='<'+subEle3+'>'+lst2[i]+'</'+subEle3+'>'
        d+='<'+subEle4+'>'+pid+'</'+subEle4+'>'
        d+='</'+subEle1+'>' 
    d=str1[:c]+d+str1[c:]
    return d
def buildTree2(rootTag,subEle1,subEle2,subEle3,subEle4,subEle5,idlist,lst1,lst2,pid):
    
    a='<'+rootTag+'>'
    for i in range(len(lst1)) :
        a+='<'+subEle1+'>'
        a+='<'+subEle2+'>'+idlist[i]+'</'+subEle2+'>'
        a+='<'+subEle3+'>'+lst1[i]+'</'+subEle3+'>'
        a+='<'+subEle4+'>'+lst2[i]+'</'+subEle4+'>'
        a+='<'+subEle5+'>'+pid+'</'+subEle5+'>'
        a+='</'+subEle1+'>' 
        
    a+='</'+rootTag+'>'
    return a

def buildTreeExtension2(str1,subEle1,subEle2,subEle3,subEle4,subEle5,idlist,lst1,lst2,l,pid):
    f=str1.rfind('</')
    d=''
    for i in range(l,len(idlist)) :
        d+='<'+subEle1+'>'
        d+='<'+subEle2+'>'+idlist[i]+'</'+subEle2+'>'
        d+='<'+subEle3+'>'+lst1[i]+'</'+subEle3+'>'
        d+='<'+subEle4+'>'+lst2[i]+'</'+subEle4+'>'
        d+='<'+subEle5+'>'+pid+'</'+subEle5+'>'
        d+='</'+subEle1+'>' 
        
    d=str1[:f]+d+str1[f:]
    return d
def buildTree3(rootTag,subEle1,subEle2,subEle3,subEle4,idlist,lst1,lst2):
    
    a='<'+rootTag+'>'
    for i in range(len(idlist)) :
        a+='<'+subEle1+'>'
        a+='<'+subEle2+'>'+idlist[i]+'</'+subEle2+'>'
        a+='<'+subEle3+'>'+lst1[i]+'</'+subEle3+'>'
        a+='<'+subEle4+'>'+lst2[i]+'</'+subEle4+'>'
        
        a+='</'+subEle1+'>' 
        
    a+='</'+rootTag+'>'
    return a


#Function to get the faculties 
def department_dalhousie():
    res = requests.get("https://www.dal.ca/academics/faculties.html")
    soup = BeautifulSoup(res.content,'html.parser')
    content=soup.find('div',attrs={"class":"contentPar parsys"})
    program_list_container=content.findAll('div',attrs={"class":"text parbase section"})

    for prg in program_list_container:
        prg_head=prg.find('h2')
        prg_br=prg_head.find('br')
        if prg_br.find('a') is not None:
            prg_txt=prg_br.find('a')
            programs_list.append(prg_txt.text)

    for prg in program_list_container:  
        prg_head=prg.find('h2')
        prg_a=prg_head.find('a')
        if prg_a is not None:
            prg_bl=prg_a.find('br')
            if prg_bl is not None and len(prg_bl.text)>2:
                programs_list.append(prg_bl.text)
            


    programs_list.append("Agriculture")            
    
    #Populate the department Ids
    program_Id=[]
    for count in range(len(programs_list)):
        if programs_list[count] is not (''):
            program_Id.append('P'+str(count))
    str1=buildTree("Departments", "Department", "DepartmentId", "DepartmentName",program_Id,programs_list)
    f1=open("Departments.xml","w",encoding='utf-8') 
    f1.write(str1)
    f1.close()
    
    
#Function to get the under graduate and graduate programs
def program_type_lists():
    #Architecture and Planning Graduate and UnderGraduate Programs
    res = requests.get("https://www.dal.ca/faculty/architecture-planning/about.html")
    soup = BeautifulSoup(res.content,'html.parser')
    content=soup.find('div',attrs={"class":"text parbase section"})
    grad_list=content.findAll('a')
    for grd in grad_list:
        if grd is not None:
            g1=grd.text.replace('\n','')
            if g1.find("Bachelor")!=-1:
                underGraduatePrograms.append(g1)
            if g1.find("Master")!=-1:
                graduatePrograms.append(g1)
    #Populating UGID
    Bachelor_Id=[]
    for countU in range(len(underGraduatePrograms)):
        if underGraduatePrograms[countU] is not (''):
            Bachelor_Id.append('B'+str(countU))
    #Populating GraduateID
    Master_Id=[]
    for countM in range(len(graduatePrograms)):
        if graduatePrograms[countM] is not (''):
            Master_Id.append('M'+str(countM))
    us=buildTree1("UnderGraduatePrograms","UG","UGID","UnderGraduateProgramName","DepartmentId",Bachelor_Id,underGraduatePrograms,"P0")
    ms=buildTree1("GraduatePrograms", "GraduateProgram", "GraduateId", "GraduateProgramName", "DepartmentId", Master_Id, graduatePrograms, "P0")
    count_B=len(Bachelor_Id)
    count_M=len(Master_Id)
    

    
    #Faculty of Arts and Science
    res1 = requests.get("https://www.dal.ca/faculty/arts/programs.html")
    soup1 = BeautifulSoup(res1.content,'html.parser')
    content1=soup1.find('div',attrs={"class":"contentPar parsys"})
    arts_list=content1.findAll('div',attrs={"class":"text parbase section"})
   
    arts_Ugraduate=arts_list[0].findAll('a')
    arts_graduate=arts_list[1].findAll('li')
    
    
    for artG in arts_Ugraduate:
        if artG is not None:
            underGraduatePrograms.append(artG.text)
    for artH in arts_graduate:
        if artH is not None:
            graduatePrograms.append(artH.text)
    for x in range(countU+1,len(underGraduatePrograms)):
        if underGraduatePrograms[x] is not (''):
            Bachelor_Id.append('B'+str(x))
    
    for y in range(countM+1,len(graduatePrograms)):
        if graduatePrograms[y] is not(''):
            Master_Id.append('M'+str(y))
    us=buildExtension(us,"UG","UGID","UnderGraduateProgramName","DepartmentId",Bachelor_Id,underGraduatePrograms,count_B,"P1")
    ms=buildExtension(ms, "GraduateProgram", "GraduateId", "GraduateProgramName", "DepartmentId", Master_Id, graduatePrograms,count_M ,"P1")
    count_B=len(Bachelor_Id)
    count_M=len(Master_Id)
      
   
    #Faculty of Computer Science
    res2 = requests.get("https://www.dal.ca/faculty/computerscience/undergraduate-programs.html")
    soup2 = BeautifulSoup(res2.content,'html.parser')
    content2=soup2.find('div',attrs={"class":"contentPar parsys"})
    cs_list1=content2.findAll('div',attrs={"class":"text parbase section"})
    cs_ug=cs_list1[0].findAll('a')
    
    for csU in cs_ug:
        if csU is not None:
            underGraduatePrograms.append(csU.text)
    
    res2 = requests.get("https://www.dal.ca/faculty/computerscience/graduate-programs/grad-handbook/how-to-apply.html")
    soup2 = BeautifulSoup(res2.content,'html.parser')
    content2=soup2.find('div',attrs={"class":"contentPar parsys"})
    cs_list1=content2.findAll('div',attrs={"class":"text parbase section"})  
     
    for csG in cs_list1:
        if csG.find('p') is not None:
            if csG.find('p').find('b') is not None:
                if csG.find('p').find('b').find('a') is not None and csG.find('p').find('b').find('a').text.find("Master")!=-1:
                    graduatePrograms.append(csG.find('p').find('b').find('a').text)
    
    for u in range(x+1,len(underGraduatePrograms)):
        if underGraduatePrograms[u] is not (''):
            Bachelor_Id.append('B'+str(u))
    
    for v in range(y+1,len(graduatePrograms)):
        if graduatePrograms[v] is not(''):
            Master_Id.append('M'+str(v))
    
    us=buildExtension(us,"UG","UGID","UnderGraduateProgramName","DepartmentId",Bachelor_Id,underGraduatePrograms,count_B,"P3")
    ms=buildExtension(ms, "GraduateProgram", "GraduateId", "GraduateProgramName", "DepartmentId", Master_Id, graduatePrograms,count_M ,"P3")
    count_B=len(Bachelor_Id)
    count_M=len(Master_Id)
    
   
    #Programs in Dentistry
    res3 = requests.get("https://www.dal.ca/faculty/dentistry/programs.html")
    soup3 = BeautifulSoup(res3.content,'html.parser')
    content3=soup3.find('div',attrs={"class":"contentPar parsys"})
    dnt_list1=content3.find('div',attrs={"class":"text parbase section"})
    pTag=dnt_list1.findAll('p')
    dnt_ug=pTag[0].findAll('a')
    for a in dnt_ug:
        underGraduatePrograms.append(a.text)
    
    for z in range(u+1,len(underGraduatePrograms)):
        if underGraduatePrograms[z] is not (''):
            Bachelor_Id.append('B'+str(z))
    us=buildExtension(us,"UG","UGID","UnderGraduateProgramName","DepartmentId",Bachelor_Id,underGraduatePrograms,count_B,"P4")
    ms=buildExtension(ms, "GraduateProgram", "GraduateId", "GraduateProgramName", "DepartmentId", Master_Id, graduatePrograms,count_M ,"P4")
    count_B=len(Bachelor_Id)
    count_M=len(Master_Id)

    
    
    #Faculty of Engineering
    res4 = requests.get("https://www.dal.ca/faculty/engineering/programs.html")
    soup4 = BeautifulSoup(res4.content,'html.parser')
    content4=soup4.find('div',attrs={"class":"contentPar parsys"})
    eng_list=content4.find('div',attrs={"class":"text parbase section"})

    eng_u=eng_list.find('ul')
    eng_listU=eng_u.findAll('li')
    
   
    for a in eng_listU:
        if a is not None:
            underGraduatePrograms.append(a.text)
            
    
    for q in range(z+1,len(underGraduatePrograms)):
        if underGraduatePrograms[q] is not (''):
            Bachelor_Id.append('B'+str(q))        
    
    res5 = requests.get("https://www.dal.ca/faculty/engineering/programs/graduate-studies/graduate_programs.html")
    soup5 = BeautifulSoup(res5.content,'html.parser')
    content5=soup5.find('div',attrs={"class":"contentPar parsys"})
    eng_Glist=content5.findAll('div',attrs={"class":"expandingSubsection section"}) 
    for a in eng_Glist:
        if a.find('h4') is not None:
            graduatePrograms.append(a.find('h4').text)
    for w in range(v+1,len(graduatePrograms)):
        if graduatePrograms[w] is not(''):
            Master_Id.append('M'+str(w))
    
    us=buildExtension(us,"UG","UGID","UnderGraduateProgramName","DepartmentId",Bachelor_Id,underGraduatePrograms,count_B,"P5")
    ms=buildExtension(ms, "GraduateProgram", "GraduateId", "GraduateProgramName", "DepartmentId", Master_Id, graduatePrograms,count_M ,"P5")
    count_B=len(Bachelor_Id)
    count_M=len(Master_Id)



    #Faculty of Health
    res6 = requests.get("https://www.dal.ca/faculty/health/programs.html")
    soup6 = BeautifulSoup(res6.content,'html.parser')
    content6=soup6.find('div',attrs={"class":"contentPar parsys"})
    h_list=content6.findAll('ul')
    h_u=h_list[0].findAll('li')
    for a  in h_u:
        if a is not None:
            underGraduatePrograms.append(a.text)
    h_g=h_list[1].findAll('li')
    for b in h_g:
        if b is not None:
            graduatePrograms.append(b.text)
    
    for e in range(q+1,len(underGraduatePrograms)):
        if underGraduatePrograms[e] is not (''):
            Bachelor_Id.append('B'+str(e))              
    for r in range(w+1,len(graduatePrograms)):
        if graduatePrograms[r] is not(''):
            Master_Id.append('M'+str(r))    
    us=buildExtension(us,"UG","UGID","UnderGraduateProgramName","DepartmentId",Bachelor_Id,underGraduatePrograms,count_B,"P11")
    ms=buildExtension(ms, "GraduateProgram", "GraduateId", "GraduateProgramName", "DepartmentId", Master_Id, graduatePrograms,count_M ,"P11")
    
    count_B=len(Bachelor_Id)
    count_M=len(Master_Id)
   
    
    #Faculty of Management
    res7 = requests.get("https://www.dal.ca/faculty/management/programs.html")
    soup7 = BeautifulSoup(res7.content,'html.parser')
    content7=soup7.find('div',attrs={"class":"containerTwoColumn section"})
    m_u=content7.findAll('li')
    for a in m_u:
        underGraduatePrograms.append(a.text)
    con=soup7.find('div',attrs={"class":"contentPar parsys"})
    
    m_gt=con.findAll('div',attrs={"class":"text parbase section"})
    
    
    m_agt=m_gt[3].findAll('a')
    
    for b in m_agt:
        if b.text is not (''):
            graduatePrograms.append(b.text)
    for t in range(e+1,len(underGraduatePrograms)):
        if underGraduatePrograms[t] is not (''):
            Bachelor_Id.append('B'+str(t))              
    for u in range(r+1,len(graduatePrograms)):
        if graduatePrograms[u] is not(''):
            Master_Id.append('M'+str(u)) 
    us=buildExtension(us,"UG","UGID","UnderGraduateProgramName","DepartmentId",Bachelor_Id,underGraduatePrograms,count_B,"P8")
    ms=buildExtension(ms, "GraduateProgram", "GraduateId", "GraduateProgramName", "DepartmentId", Master_Id, graduatePrograms,count_M ,"P8")
   
    count_B=len(Bachelor_Id)
    count_M=len(Master_Id) 


    
    #Faculty of Medicine
    
    res8 = requests.get("https://medicine.dal.ca/programs.html")
    soup8 = BeautifulSoup(res8.content,'html.parser')
    content8=soup8.find('div',attrs={"class":"contentPar parsys"})
    md_list=content8.findAll('div',attrs={"class":"text parbase section"})
    underGraduatePrograms.append(md_list[0].find('h2').find('b').text)
    graduatePrograms.append(md_list[1].find('h2').text)
    graduatePrograms.append(md_list[3].find('h2').find('b').text)
    
          
    for i in range(t+1,len(underGraduatePrograms)):
        if underGraduatePrograms[i] is not (''):
            Bachelor_Id.append('B'+str(i))              
    for o in range(u+1,len(graduatePrograms)):
        if graduatePrograms[o] is not(''):
            Master_Id.append('M'+str(o)) 
    us=buildExtension(us,"UG","UGID","UnderGraduateProgramName","DepartmentId",Bachelor_Id,underGraduatePrograms,count_B,"P9")
    ms=buildExtension(ms, "GraduateProgram", "GraduateId", "GraduateProgramName", "DepartmentId", Master_Id, graduatePrograms,count_M ,"P9")
    
    count_B=len(Bachelor_Id)
    count_M=len(Master_Id) 
 
   
   
    #Faculty of Science
    res9 = requests.get("https://www.dal.ca/faculty/science/programs/AcademicPrograms.html")
    soup9 = BeautifulSoup(res9.content,'html.parser')
    content9=soup9.find('div',attrs={"class":"contentPar parsys"})
    s_list=content9.findAll('div',attrs={"class":"text parbase section"})
    s_uglist=s_list[1].findAll('td')
    s_ulist=s_uglist[0].findAll('a')
    s_glist=s_uglist[1].findAll('a')
    
    for a in s_ulist:
        if a is not None:
            underGraduatePrograms.append(a.text)
    
    for b in s_glist:
        if b is not None:
            graduatePrograms.append(b.text)
    
    for p in range(i+1,len(underGraduatePrograms)):
        if underGraduatePrograms[p] is not (''):
            Bachelor_Id.append('B'+str(p))              
    for s in range(o+1,len(graduatePrograms)):
        if graduatePrograms[s] is not(''):
            Master_Id.append('M'+str(s))  
    us=buildExtension(us,"UG","UGID","UnderGraduateProgramName","DepartmentId",Bachelor_Id,underGraduatePrograms,count_B,"P10")
    ms=buildExtension(ms, "GraduateProgram", "GraduateId", "GraduateProgramName", "DepartmentId", Master_Id, graduatePrograms,count_M ,"P10")
    
    count_B=len(Bachelor_Id)
    count_M=len(Master_Id) 
   
    #Faculty of Agriculture
    res10 = requests.get("https://www.dal.ca/faculty/agriculture/programs.html")
    soup10 = BeautifulSoup(res10.content,'html.parser')
    content10=soup10.find('div',attrs={"class":"col-first"})
    a_list=content10.findAll('a')
    
    for i in range(len(a_list)-1):
        if a_list[i].text is not None:
            underGraduatePrograms.append(a_list[i].text)
    graduatePrograms.append(a_list[-1].text)
    
    for d in range(p+1,len(underGraduatePrograms)):
        if underGraduatePrograms[d] is not (''):
            Bachelor_Id.append('B'+str(d))              
    for f in range(s+1,len(graduatePrograms)):
        if graduatePrograms[f] is not(''):
            Master_Id.append('M'+str(f))  
    us=buildExtension(us,"UG","UGID","UnderGraduateProgramName","DepartmentId",Bachelor_Id,underGraduatePrograms,count_B,"P12")
    ms=buildExtension(ms, "GraduateProgram", "GraduateId", "GraduateProgramName", "DepartmentId", Master_Id, graduatePrograms,count_M ,"P12")
    
    f2=open("UnderGraduatePrograms.xml","w",encoding='utf-8') 
    f2.write(us.replace("&",""))
    f2.close()
    f3=open("GraduatePrograms.xml","w",encoding='utf-8') 
    f3.write(ms.replace("&",""))
    f3.close()
    print(ms)

#Function to get the employee list
def employee_list():
    #Employee List of Agriculture Department
    res = requests.get("https://www.dal.ca/faculty/agriculture/animal-science-aquaculture/faculty-staff/our-staff.html")
    soup = BeautifulSoup(res.content,'html.parser')
    content=soup.find('div',attrs={"class":"contentPar parsys"})
    e_alst=content.find('div',attrs={"class":"text parbase section"})
    e_a=e_alst.findAll('tr')
    
    for a in range(1,len(e_a)):
        b=e_a[a].findAll('td')
        c=b[0].text.split(' ')
        empFrstName.append(c[0])
        empScndName.append(c[1])
    #Populating Employee Ids
    Employee_Id=[]
    for countU in range(len(empFrstName)):
        if empFrstName[countU] is not (''):
            Employee_Id.append('E'+str(countU))
    es=buildTree2("Employees", "Employee", "EmpId", "FirstName", "LastName", "Department", Employee_Id, empFrstName, empScndName, "P12")
    count_E=len(Employee_Id) 
    
    
    #Employee List of Architecture and Planning
    res = requests.get("https://www.dal.ca/faculty/architecture-planning/faculty-staff/staff.html")
    soup = BeautifulSoup(res.content,'html.parser')
    content=soup.find('div',attrs={"class":"contentPar parsys"})
    e_aplst=content.find('div',attrs={"class":"text parbase section"})
    e_ap=e_aplst.findAll('tr')
    for i in range(len(e_ap)):
        b=e_ap[i].findAll('td')
        c=b[0].text.split(' ')
        empFrstName.append(c[0])
        empScndName.append(c[1])
    
    for x in range(countU+1,len(empFrstName)):
        if empFrstName[x] is not (''):
            Employee_Id.append('E'+str(x)) 
             
    
    es=buildTreeExtension2(es, "Employee", "EmpId", "FirstName", "LastName", "Department", Employee_Id, empFrstName, empScndName,count_E, "P0") 
    count_E=len(Employee_Id) 
    
    #Employees of Arts and Science
    
    res = requests.get("https://www.dal.ca/faculty/architecture-planning/faculty-staff/staff.html")
    soup = BeautifulSoup(res.content,'html.parser')
    content=soup.find('div',attrs={"class":"contentPar parsys"})
    e_aslst=content.findAll('div',attrs={"class":"text parbase section"})
    for a in e_aslst:
        b=a.findAll('tr')
        for i in range(len(b)):
            c=b[i].findAll('td')
            d=c[0].text.split(' ')
            empFrstName.append(d[0])
            empScndName.append(d[1])
    for q in range(x+1,len(empFrstName)):
        if empFrstName[q] is not (''):
            Employee_Id.append('E'+str(q)) 
    es=buildTreeExtension2(es, "Employee", "EmpId", "FirstName", "LastName", "Department", Employee_Id, empFrstName, empScndName,count_E, "P1") 
    count_E=len(Employee_Id)   
    
    
    #Employees of Computer Science
    temp1=[]
    temp2=[]
    res = requests.get("https://www.dal.ca/faculty/computerscience/faculty-staff.html")
    soup = BeautifulSoup(res.content,'html.parser')
    content=soup.find('div',attrs={"class":"contentPar parsys"})
    e_cslst=content.findAll('div',attrs={"class":"text parbase section"})
    for a  in e_cslst:
        b=a.findAll('tr')
        for i in range(len(b)):
            c=b[i].findAll('td')
            if len(c)>2:
               
                m=c[0].find('a')
                if m is not None:
                    temp1.append(m.text)
                if c[0].find('a') is None:
                    temp2.append(c[0].text)
    
    
    temp1=[t.replace('Dr. ','') for t in temp1] 
    temp1=[t.replace('Mr. ','') for t in temp1]
    temp1=[t.replace('Ms. ','') for t in temp1]
    temp2=[t.replace('Dr. ','') for t in temp2] 
    temp2=[t.replace('Mr. ','') for t in temp2]
    temp2=[t.replace('Ms. ','') for t in temp2]
    for i in temp1:
        b=i.split(' ')
        empFrstName.append(b[0])
        empScndName.append(b[1])
    for i in temp2:
        b=i.split(' ')
        empFrstName.append(b[0])
        empScndName.append(b[1])
    for w in range(q+1,len(empFrstName)):
        if empFrstName[w] is not (''):
            Employee_Id.append('E'+str(w)) 
    es=buildTreeExtension2(es, "Employee", "EmpId", "FirstName", "LastName", "Department", Employee_Id, empFrstName, empScndName,count_E, "P3")   
    count_E=len(Employee_Id)
    
    #Employees of Engineering
    res = requests.get("https://www.dal.ca/faculty/engineering/electrical/faculty-staff.html")
    soup = BeautifulSoup(res.content,'html.parser')
    content=soup.find('div',attrs={"class":"contentPar parsys"})
    e_eslst=content.findAll('div',attrs={"class":"text parbase section"})
    b= e_eslst[5]
    c=b.findAll('tr')
    for i in range(len(c)):
        d=c[i].findAll('td')
        e=d[0]
        #to eliminate "name" heading which is also inside table data
        if e.text is not None and len(e.text)>5:
            f=e.text.split(" ")
            empFrstName.append(f[0])
            empScndName.append(f[1])
            
    for e in range(w+1,len(empFrstName)):
        if empFrstName[e] is not (''):
            Employee_Id.append('E'+str(e)) 
    es=buildTreeExtension2(es, "Employee", "EmpId", "FirstName", "LastName", "Department", Employee_Id, empFrstName, empScndName,count_E, "P5")
    count_E=len(Employee_Id)
    
    #Employees of Health Department
    res = requests.get("https://www.dal.ca/faculty/health/health-humanperformance/faculty-staff/our-staff.html")
    soup = BeautifulSoup(res.content,'html.parser')
    content=soup.find('div',attrs={"class":"contentPar parsys"})
    e_hslst=content.find('div',attrs={"class":"text parbase section"})
    a=e_hslst.findAll('h3')
    for i  in a[:-1]:
        b=i.text.split(" ")
        empFrstName.append(b[0])
        empScndName.append(b[1])
     
    for r in range(e+1,len(empFrstName)):
        if empFrstName[r] is not (''):
            Employee_Id.append('E'+str(r))    
    es=buildTreeExtension2(es, "Employee", "EmpId", "FirstName", "LastName", "Department", Employee_Id, empFrstName, empScndName,count_E, "P11")
    count_E=len(Employee_Id)  
    res = requests.get("https://www.dal.ca/faculty/health/nursing/faculty-staff/staff.html")
    soup = BeautifulSoup(res.content,'html.parser')
    content=soup.find('div',attrs={"class":"contentPar parsys"})
    e_aslst=content.findAll('div',attrs={"class":"text parbase section"})
    for a in e_aslst:
        b=a.findAll('tr')
        for i in range(len(b)):
            c=b[i].findAll('td')
            d=c[0].find('p')
            if d is not None:
                g=d.text.split(" ")
                empFrstName.append(g[0])
                empScndName.append(g[1])
    
     
    for s in range(r+1,len(empFrstName)):
        if empFrstName[s] is not (''):
            Employee_Id.append('E'+str(s)) 
    es=buildTreeExtension2(es, "Employee", "EmpId", "FirstName", "LastName", "Department", Employee_Id, empFrstName, empScndName,count_E, "P11")
    count_E=len(Employee_Id) 
    
    f1=open("Employees.xml","w",encoding='utf-8') 
    f1.write(es)
    f1.close()
    
    
    
def research_list():
    res = requests.get("https://www.dal.ca/research/centres_and_institutes.html")
    soup = BeautifulSoup(res.content,'html.parser')
    content=soup.find('div',attrs={"class":"contentPar parsys"})
    e_rslst=content.find('div',attrs={"class":"text parbase section"})
    research_id=[]
    research_institute=[]
    research_area=[]
    
    h=0
    r_hd=e_rslst.findAll('h2')
    r_li=e_rslst.findAll('ul')
    ls_sep=[]
    
    for j in r_li:
        a=j.findAll('a')
        h=0
        for x in a:
            #print(x.text)
            research_area.append(x.text.replace('&',''))
            h+=1
        ls_sep.append(h)
    for i in range(len(r_hd)):
        k=r_hd[i].text.replace('&','').replace(':','').replace(',','')
        
        
        research_institute.extend([k]*ls_sep[i])
    
    for s in range(len(research_area)):
        if research_area[s] is not (''):
            research_id.append('R'+str(s)) 

    rs=buildTree3("Researches","Research","ID","Institute","Area",research_id,research_institute,research_area)
    f1=open("Research.xml","w",encoding='utf-8') 
    f1.write(rs)
    f1.close()  
      
                
            
    
                
#Function to get the Departments.xml
department_dalhousie()
#Function to get the UnderGraduatePrograms.xml and GraduatePrograms.xml
program_type_lists()
#Function to get the Employees.xml
employee_list()
#Function to get the Research.xml
research_list()    

            
    
    
        

    