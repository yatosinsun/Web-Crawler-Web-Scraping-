# Open the Terminal (cmd)
# Use this code: pip install bs4
# Enter
# When the successfully loading, come here to this Editor and follow the steps below 

# Firstly we add to request package from coming to BeautifulSoup Library
import requests
#(1) from bs4 import BeautifulSoup  #(Description below, follow, delete comments when you come back, activate)
#(2) import time  #(Description below, follow, delete comments when you come back, activate)

# Take the link of the site we want to scrape and define it into a variable.
URL = 'https://www.amazon.com.tr/Lenovo-Bilgisayar%C4%B1-i5-13420H-RTX4050-82XV00G5TX/dp/B0CCNT1YKF/ref=pd_day0_d_sccl_2_4/262-8543975-1536823?pd_rd_w=zjvvf&content-id=amzn1.sym.17a3f55d-c94e-4bd8-9dc5-ae84ad3b2e0d&pf_rd_p=17a3f55d-c94e-4bd8-9dc5-ae84ad3b2e0d&pf_rd_r=J2DZ8AN8VV32Q9M1BE9F&pd_rd_wg=kM2Oj&pd_rd_r=c7940bfc-7d32-4cf5-a843-4ef94ceaf1c1&pd_rd_i=B0CCNT1YKF&psc=1'

# When connecting to the page with Python, the site asks for our user agent information.   
# How do you find the your user agent? 
# Write to Google : my user agent 
# Click now ! You find !
# copy and paste to here: {"User-Agent":".....here...."}
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"}
# This is necessary for the web page to recognize us. Without this information, the page may block.
# Now we can link to the page.
# We can also transfer this connection we have established to a variable.
# The Request library will come into play here.
# By making a link here, we can download the page content as it is.
page = requests.get(URL, headers=headers)
# Here we define what it will bring with get.
# First of all, what it will bring, that is, the page and the headers information it will use when going here,
# will give the headers information we defined above.
# After these, we will establish a link to the page. But we cannot see the content.
# We will create a variable to see the content.
# There are different methods to retrieve content. But there are packages in the BS4 library that we can use.
# It will be added first and it will be easier to process through it.
# For this we will use the BeautifulSoup package from the bs4 library.
# For this process, now activate comment number (1) above.
# The expression that should be written will be as follows: from bs4 import BeautifulSoup
# Now, while getting the content, we define BeautifulSoup and define the content coming from the page into it.
# But since the website is in html structure, we need to specify this as well.
# But let's check the html structure of this site.
# When we open the page in Google, right-click and click "View Page Source" (Ctrl + U), we view the source codes of the page.
# You will see that there are many related and irrelevant objects here. But you need to separate them.
# BeautifulSoup comes into play at this point.
# We specify the use of 'html.parser' when fetching this page.
content = BeautifulSoup(page.content, 'html.parser')
# Now let's run it to test it.
print(content)
# Now downloaded the source codes of the page. But we need to parse the data we want from here.
# To do this, we go to the page again, right click and click "Review".
# In the opened tab, we will determine fields such as the name and price of the product from the "Elements" content.
# For example, when you first search for the name of the product, you will see the extension below.
# When you open this, the product name appears.

"""
 <div id="titleSection" class="a-section a-spacing-none"> <h1 id="title" class="a-size-large a-spacing-none"> 
    <span id="productTitle" class="a-size-large product-title-word-break">        
        Lenovo LOQ 15IRH8 Oyuncu Bilgisayarı, 15.6" FHD 144 Hz, Intel Core i5-13420H, 8GB RAM, 512GB SSD, RTX4050 6GB Ekran Kartı, FreeDOS, 82XV00G5TX       
    </span>       </h1> <div id="expandTitleToggle" class="a-section a-spacing-none expand aok-hidden"></div>  </div>                                
</div>

Here we are interested in the <span part. When we look at this, the product name appears as follows.

Lenovo LOQ 15IRH8 Oyuncu Bilgisayarı, 15.6" FHD 144 Hz, Intel Core i5-13420H, 8GB RAM, 512GB SSD, RTX4050 6GB Ekran Kartı, FreeDOS, 82XV00G5TX
"""

# Here are the parts that are important to us. First, we must use the "id" part.
# We will create a variable for this. We have the "content" variable that contains the information of this page.
# Now we need to search within this variable, that is, on this web page, to find what we are interested in.
productName = content.find(id='productTitle').get_text().strip()
# As above, we search in "content" with "find".
# What we will look for is; We specify it as "object whose id value is productTitle".
# Since we want it to fetch this as text, we add the "get_text()" command.
# Since there are often spaces in HTML pages, we add "strip()" and write the text without spaces above and below.
# We add the fetch command only as text.
print(productName)
#Let's check the output by printing in the terminal.

# Now we have the name of the product, let's also want to get its price.
# To do this, we go to the page again, right click and click "Review".
# In the opened tab, we will determine the price of the product from the "Elements" content.
# When we right click on it and click "Copy Elements" the following appears.

"""
<div id="corePriceDisplay_desktop_feature_div" class="celwidget" data-feature-name="corePriceDisplay_desktop" data-csa-c-type="widget" data-csa-c-content-id="corePriceDisplay_desktop" data-csa-c-slot-id="corePriceDisplay_desktop_feature_div" data-csa-c-asin="B0CCNT1YKF" data-csa-c-is-in-initial-active-row="false" data-csa-c-id="6xjtss-ga66uy-xb5w7e-8n71om" data-cel-widget="corePriceDisplay_desktop_feature_div">
                                              <style type="text/css">
    .savingPriceOverride {
        color:#CC0C39!important;
        font-weight: 300!important;
    }
    .savingPriceOverrideEdlpT1 {
        color:#565959!important;
        font-weight: 700!important;
    }
    .savingPriceOverrideEdlpT2 {
        color:#565959!important;
        font-weight: 300!important;
    }
    .savingPriceOverrideEdlpT3 {
        color:#CC0C39!important;
        font-weight: 700!important;
    }
</style>

                                                                         <div class="a-section a-spacing-none aok-align-center aok-relative"> <span class="aok-offscreen">   34.999,00&nbsp;TL  </span>                   <span class="a-price aok-align-center reinventPricePriceToPayMargin priceToPay" data-a-size="xl" data-a-color="base"><span class="a-offscreen"> </span><span aria-hidden="true"><span class="a-price-whole">34.999<span class="a-price-decimal">,</span></span><span class="a-price-fraction">00</span><span class="a-price-symbol">TL</span></span></span>              <span id="taxInclusiveMessage" class="a-size-mini a-color-base aok-align-center aok-nowrap">  </span>          </div>  <div class="a-section a-spacing-small aok-align-center">    <span>   <span class="a-size-small aok-align-center basisPriceLegalMessage">                  <style type="text/css">
    .reinventPrice_legalMessage_icon {
        width: 12px;
        fill: #969696;
        vertical-align: middle;
        padding-bottom: 2px;
    }

    .reinventPrice_legalMessage_icon:hover {
        fill: #555555;
    }
</style>

<script type="text/javascript">
    P.when('A', 'a-popover').execute('a-popover-count', function (A) {
        A.declarative('a-popover', 'mouseenter', function() {
            ue.count("tooltip.popover.opened", 1);
        });
    });
</script>
  </span> </span> </div>                                        </div>

"""
# But when we right click and say "Copy Xpath", "id" will automatically appear.

"""
//*[@id="corePriceDisplay_desktop_feature_div"]
"""
# In summary, what we are actually looking for is the following.
"""
id="corePriceDisplay_desktop_feature_div"

<span class="a-price aok-align-center reinventPricePriceToPayMargin priceToPay" data-a-size="xl" data-a-color="base"><span class="a-offscreen"> </span>< span aria-hidden="true"><span class="a-price-whole">34.999<span class="a-price-decimal">,</span></span><span class="a- price-fraction">00</span><span class="a-price-symbol">TL</span></span></span>
"""
# Now we will perform this search in a similar way.
price = content.find(id='corePriceDisplay_desktop_feature_div').get_text().strip()
print(price)
# The value we find in the terminal contains the period, comma and currency value. 
# We need to make this integer.
priceConverted = int(price[0:6].replace('.',''))
# Here we enter the integer command with "int".
# Then, we find the number of values starting from which index in the "price" variable and add it to the starting index.
# Next '.' He uses the "replace" command to get rid of the "." statement. Because we don't want it to replace anything.
# We put the expression ''. If we wanted another symbol, we could write it inside quotes.
print(priceConverted)

# Now we can set up an if loop to compare this value (to understand a real discount).

     if(priceConverted < 30000):
         print(f"{priceConverted} Lira {productName} price decreased by 15%!!!")
     else:
         print(f"{priceConverted} Lira {productName} has not dropped yet")
     # We will use "format text" to write the product name. That's why we use f{}.
     # At this stage, close the print functions above and see only the message of the if block.

"""
  It would be more accurate if we turn this into a function. Therefore starting from "URL" above
         Comment the entire flow and proceed with the form below.
"""

def productControl():
    URL = 'https://www.amazon.com.tr/Lenovo-Bilgisayar%C4%B1-i5-13420H-RTX4050-82XV00G5TX/dp/B0CCNT1YKF/ref=pd_day0_d_sccl_2_4/262-8543975-1536823?pd_rd_w=zjvvf&content-id=amzn1.sym.17a3f55d-c94e-4bd8-9dc5-ae84ad3b2e0d&pf_rd_p=17a3f55d-c94e-4bd8-9dc5-ae84ad3b2e0d&pf_rd_r=J2DZ8AN8VV32Q9M1BE9F&pd_rd_wg=kM2Oj&pd_rd_r=c7940bfc-7d32-4cf5-a843-4ef94ceaf1c1&pd_rd_i=B0CCNT1YKF&psc=1'
    # When connecting to the page with Python, the site asks for our user information.   
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"}
    page = requests.get(URL, headers = headers)
    content = BeautifulSoup(page.content,'html.parser')
    #print(content)
    #productTitle
    productName = content.find(id='productTitle').get_text().strip()
    #print(productName)
    #corePriceDisplay_desktop_feature_div
    price = content.find(id='corePriceDisplay_desktop_feature_div').get_text()
    priceConverted = int(price[1:6].replace('.',''))
    #print(priceConverted)

    if(priceConverted < 30000):
        print(f"{priceConverted} Lira {productName} price decreased by 15%!!!")
    else:
        print(f"{priceConverted} Lira {productName} has not dropped yet")

# Now we can track this regularly by putting a timer.
# But first we need to add the "time" library to do this.
# For this process, now activate comment number (2) above.
# The expression that should be written will be as follows: import time

# If it calls repeatedly, it may lock the computer.
# Therefore, if you trust your computer, you can reduce the seconds frequency.

# The timer works in "seconds" and when we say "5" it perceives it as "every 5 seconds".
# If we want 1 minute, "60"; If we want 5 minutes, we write "60*5".
# If we want 1 hour, "60 * 60"; If we want 1 day, we can write it as "60 * 60 * 24".
        
while(True):
    productControl()
    time.sleep(60)

# Now it downloads the site every 1 minute and returns us the message in the if block by running the "productControl" function.

# Now, if we write all the codes regularly, it will be as follows.
# The codes below are the codes we need to reach the final result.
# You can take this block and run it in a new .py file and personalize the codes.
# First of all, do not forget to install the BeautifulSoup library from the terminal.
# Do not try to run it again within this page!!!
    
import requests
from bs4 import BeautifulSoup 
import time  

def productControl():
    URL = 'https://www.amazon.com.tr/Lenovo-Bilgisayar%C4%B1-i5-13420H-RTX4050-82XV00G5TX/dp/B0CCNT1YKF/ref=pd_day0_d_sccl_2_4/262-8543975-1536823?pd_rd_w=zjvvf&content-id=amzn1.sym.17a3f55d-c94e-4bd8-9dc5-ae84ad3b2e0d&pf_rd_p=17a3f55d-c94e-4bd8-9dc5-ae84ad3b2e0d&pf_rd_r=J2DZ8AN8VV32Q9M1BE9F&pd_rd_wg=kM2Oj&pd_rd_r=c7940bfc-7d32-4cf5-a843-4ef94ceaf1c1&pd_rd_i=B0CCNT1YKF&psc=1'
    # When connecting to the page with Python, the site asks for our user information.   
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"}
    page = requests.get(URL, headers = headers)
    content = BeautifulSoup(page.content,'html.parser')
    #print(content)
    #productTitle
    productName = content.find(id='productTitle').get_text().strip()
    #print(productName)
    #corePriceDisplay_desktop_feature_div
    price = content.find(id='corePriceDisplay_desktop_feature_div').get_text()
    priceConverted = int(price[1:6].replace('.',''))
    #print(priceConverted)

    if(priceConverted < 30000):
        print(f"{priceConverted} Lira {productName} price decreased by 15%!!!")
    else:
        print(f"{priceConverted} Lira {productName} has not dropped yet")

while(True):
    productControl()
    time.sleep(60)
