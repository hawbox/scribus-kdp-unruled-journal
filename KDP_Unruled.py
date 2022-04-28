import scribus
def gutter_margin(total_page):
  if int(total_page) in range(24,151):
    margin = float(0.375)
  elif int(total_page) in range(151,301):
    margin = float(0.5)
  elif int(total_page) in range(301,501):
    margin = float(0.625)
  elif int(total_page) in range(501,701):
    margin = float(0.75)
  elif int(total_page) in range(701,829):
    margin = float(0.875)
  else:
    scribus.messageBox("Warning","The page number you enter is out of range!")
  return margin
gutter = gutter_margin(120)
margin = (gutter,0.25,0.25,0.25)
def createPages(num):
 for i in range(1,num+1):
   scribus.gotoPage(i)
   t,inside,outside,b = scribus.getPageMargins()
   w,h = scribus.getPageSize()
   leftmargin = outside if scribus.currentPage() % 2 == 0 else inside
   date = scribus.createText(leftmargin,t,0.8,scribus.inch*16)
   scribus.setText("Date:",date)
   currPage = scribus.createText(leftmargin+(w-inside-outside)-0.35,t,0.35,scribus.inch*16)
   scribus.setText(str(scribus.currentPage()),currPage)
   scribus.setTextAlignment(scribus.ALIGN_RIGHT,currPage)
   underline = scribus.createLine(leftmargin,t+scribus.inch*16,leftmargin+(w-inside-outside),t+scribus.inch*16)
   scribus.setLineWidth(0.01,underline)
askforPages = scribus.valueDialog("Ask for Total Page Count","How many pages do you want to create")
scribus.newDocument((6,9),margin,scribus.PORTRAIT,1,scribus.UNIT_INCHES,scribus.PAGE_2,1,int(askforPages))
createPages(int(askforPages))