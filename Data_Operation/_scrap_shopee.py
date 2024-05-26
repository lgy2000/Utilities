# !/usr/bin/env python3
"""
_scrap_shopee.py

This module is used for scraping data from Shopee.

Description:
This module uses the BeautifulSoup library to parse HTML data from Shopee's website. It extracts specific data from the page, such as product details.
"""

from bs4 import BeautifulSoup

# url = 'https://shopee.com.my/cart/'

# html = requests.get(url)
html = """
<body>
<noscript>
<iframe src="https://www.googletagmanager.com/ns.html?id=GTM-WJZQSJF" height="0" width="0" style="display:none;visibility:hidden"></iframe>
<div id="main"><style id="nebula-style">:root{--nc-primary:#ee4d2d;--nc-primary-bg:#fef6f5;--nc-primary-gradient:linear-gradient(#ee4d2d,
#ff7337);--nc-secondary-blue:#0046ab;--nc-secondary-yellow:#eda500;--nc-secondary-green:#26aa99;--nc-error:#ee2c4a;--nc-error-bg:#fff4f4;--nc
-caution:#f69113;--nc-caution-bg:#fff8e4;--nc-success:#30b566;--nc-success-bg:#f7fffe;--nc-text-primary:rgba(0,0,0,
.87);--nc-text-primary-o:#212121;--nc-text-secondary:rgba(0,0,0,.65);--nc-text-secondary-o:#595959;--nc-text-tertiary:rgba(0,0,0,
.54);--nc-text-tertiary-o:#757575;--nc-text-link:#0088ff;--nc-util-mask:rgba(0,0,0,.4);--nc-util-disabled:rgba(0,0,0,
.26);--nc-util-disabled-o:#bdbdbd;--nc-util-line:rgba(0,0,0,
.09);--nc-util-line-o:#e8e8e8;--nc-util-bg:#f5f5f5;--nc-util-placeholder:#fafafa;--nc-util-pressed:rgba(0,0,0,
.05);--nt-font-regular-f:-apple-system,'HelveticaNeue','Helvetica Neue','Roboto','Droid Sans',Arial,
sans-serif;--nt-font-regular-w:400;--nt-font-medium-f:-apple-system,'HelveticaNeue-Medium','Helvetica Neue','Roboto','Droid Sans',Arial,
sans-serif;--nt-font-medium-w:500;--nt-font-bold-f:-apple-system,'HelveticaNeue-Bold','Helvetica Neue','Roboto','Droid Sans','Arial Bold',Arial,
sans-serif;--nt-font-bold-w:700;--nt-size-foot:.625rem;--nt-size-foot-l:.75rem;--nt-size-foot-lp:.75rem;--nt-size-foot-t:1rem;--nt-size-foot-tp
:1rem;--nt-size-small:.75rem;--nt-size-small-l:.875rem;--nt-size-small-lp:1.25rem;--nt-size-small-t:1.125rem;--nt-size-small-tp:1.125rem;--nt-size
-normal:.875rem;--nt-size-normal-l:1rem;--nt-size-normal-lp:1.25rem;--nt-size-normal-t:1.375rem;--nt-size-normal-tp:1.375rem;--nt-size-large:1rem
;--nt-size-large-l:1.25rem;--nt-size-large-lp:1.375rem;--nt-size-large-t:1.5rem;--nt-size-large-tp:1.5rem;--nt-size-title:1.25rem;--nt-size-title-l
:1.5rem;--nt-size-title-lp:1.5rem;--nt-size-title-t:1.875rem;--nt-size-title-tp:1.875rem;--ns-a:.25rem;--ns-b:.5rem;--ns-c:.75rem;--ns-d:1rem;--ns
-e:1.25rem;--ns-f:1.5rem;--ns-g:2.5rem;--ne-depth6:0 0 .375rem rgba(0,0,0,.06);--ne-depth9:0 0 .5625rem rgba(0,0,0,
.12);--nr-normal:.125rem;--nr-overlay:.25rem}.nt-foot{font-size:var(--nt-size-foot,.625rem);line-height:var(--nt-size-foot-l,.75rem)}.nt-foot-p{
font-size:var(--nt-size-foot,.625rem);line-height:var(--nt-size-foot-lp,.75rem)}.nt-small{font-size:var(--nt-size-small,.75rem);line-height:var(
--nt-size-small-l,.875rem)}.nt-small-p{font-size:var(--nt-size-small,.75rem);line-height:var(--nt-size-small-lp,1.25rem)}.nt-normal{font-size:var(
--nt-size-normal,.875rem);line-height:var(--nt-size-normal-l,1rem)}.nt-normal-p{font-size:var(--nt-size-normal,.875rem);line-height:var(
--nt-size-normal-lp,1.25rem)}.nt-large{font-size:var(--nt-size-large,1rem);line-height:var(--nt-size-large-l,1.25rem)}.nt-large-p{font-size:var(
--nt-size-large,1rem);line-height:var(--nt-size-large-lp,1.375rem)}.nt-title{font-size:var(--nt-size-title,1.25rem);line-height:var(
--nt-size-title-l,1.5rem)}.nt-title-p{font-size:var(--nt-size-title,1.25rem);line-height:var(--nt-size-title-lp,1.5rem)}.nt-regular{
font-family:var(--nt-font-regular-f,-apple-system,'HelveticaNeue','Helvetica Neue','Roboto','Droid Sans',Arial,sans-serif);font-weight:var(
--nt-font-regular-w,400)}.nt-medium{font-family:var(--nt-font-medium-f,-apple-system,'HelveticaNeue-Medium','Helvetica Neue','Roboto','Droid Sans',
Arial,sans-serif);font-weight:var(--nt-font-medium-w,500)}.nt-bold{font-family:var(--nt-font-bold-f,-apple-system,'HelveticaNeue-Bold',
'Helvetica Neue','Roboto','Droid Sans','Arial Bold',Arial,sans-serif);font-weight:var(--nt-font-bold-w,700)}</style><div><section class="lF2jXb" 
tabindex="-1"><button class="stardust-button u6BOJM" tabindex="10000"><span class="zV2jR+">Skip to main content</span></button></section><div 
class="shopee-progress-bar"></div><div style="display: contents;"><header class="shopee-top container-wrapper"><div class="navbar-wrapper 
container-wrapper navbar-wrapper--without-search"><nav class="container navbar"><div class="flex v-center _20ATCl"><a href="//seller.shopee.com.my" 
target="_blank" rel="noopener noreferrer" class="+t6rxm B+lcw5">Seller Centre</a><div class="shopee-drawer B+lcw5" id="pc-drawer-id-0"><a 
class="+t6rxm" href="/web/" target="_blank" rel="noopener noreferrer" id="temporaryId">Download</a></div><div class="flex +t6rxm B+lcw5 
z3pxo7">Follow us on</div><div class="flex +t6rxm _6L8cr8"><a class="qkTYhi header-navbar-background header-navbar-facebook-png" 
href="https://facebook.com/ShopeeMY" target="_blank" rel="noopener noreferrer" title="Follow us on Facebook"></a><a 
href="https://instagram.com/Shopee_MY" target="_blank" rel="noopener noreferrer" class="Hjoocb header-navbar-background 
header-navbar-instagram-png" title="Follow us on Instagram!"></a></div></div><div class="navbar__spacer"></div><ul class="navbar__links"><li 
class="navbar__link--notification navbar__link navbar__link--hoverable navbar__link--tappable"><div class="stardust-popover" id="stardust-popover2" 
tabindex="0"><div role="button" class="stardust-popover__target"><a class="W-2aSq" tabindex="-1" href="/user/notifications/order"><svg viewBox="3 
2.5 14 14" x="0" y="0" class="shopee-svg-icon icon-notification-2"><path d="m17 15.6-.6-1.2-.6-1.2v-7.3c0-.2 
0-.4-.1-.6-.3-1.2-1.4-2.2-2.7-2.2h-1c-.3-.7-1.1-1.2-2.1-1.2s-1.8.5-2.1 1.3h-.8c-1.5 0-2.8 1.2-2.8 2.7v7.2l-1.2 
2.5-.2.4h14.4zm-12.2-.8.1-.2.5-1v-.1-7.6c0-.8.7-1.5 1.5-1.5h6.1c.8 0 1.5.7 1.5 1.5v7.5.1l.6 1.2h-10.3z"></path><path d="m10 18c1 0 1.9-.6 
2.3-1.4h-4.6c.4.9 1.3 1.4 2.3 1.4z"></path></svg><div class="e326xl RaV0lX c1uTz+">2</div><span 
class="i4da+9">notifications</span></a></div></div></li><a class="navbar__link navbar__link--tappable navbar__link--hoverable navbar__link--help" 
href="https://help.shopee.com.my/my/s" target="_blank" rel="noopener noreferrer" tabindex="0"><div class="navbar__help-center-icon"><svg 
height="16" viewBox="0 0 16 16" width="16" class="shopee-svg-icon icon-help-center"><g fill="none" fill-rule="evenodd" transform="translate(
1)"><circle cx="7" cy="8" r="7" stroke="currentColor"></circle><path fill="currentColor" d="m6.871 3.992c-.814 0-1.452.231-1.914.704-.462.462-.693 
1.089-.693 1.892h1.155c0-.484.099-.858.297-1.122.22-.319.583-.473 1.078-.473.396 0 .715.11.935.33.209.22.319.517.319.902 0 
.286-.11.55-.308.803l-.187.209c-.682.605-1.1 1.056-1.243 1.364-.154.286-.22.638-.22 
1.045v.187h1.177v-.187c0-.264.055-.506.176-.726.099-.198.253-.396.462-.572.517-.451.825-.737.924-.858.275-.352.418-.803.418-1.342 
0-.66-.22-1.188-.66-1.573-.44-.396-1.012-.583-1.716-.583zm-.198 6.435c-.22 0-.418.066-.572.22-.154.143-.231.33-.231.561 0 
.22.077.407.231.561s.352.231.572.231.418-.077.572-.22c.154-.154.242-.341.242-.572s-.077-.418-.231-.561c-.154-.154-.352-.22-.583-.22z"></path></g
></svg></div><span class="navbar__link-text navbar__link--tappable navbar__link--hoverable">help</span></a><li class="navbar__link--notification 
navbar__link navbar__link--hoverable navbar__link--tappable"><div class="stardust-popover" id="stardust-popover0" tabindex="0"><div role="button" 
class="stardust-popover__target"><div class="+Z0GVP"><div class="cbylvS"><svg width="16" height="16" viewBox="0 0 16 16" fill="none" 
xmlns="http://www.w3.org/2000/svg"><path d="M8.00065 14.6667C11.6825 14.6667 14.6673 11.6819 14.6673 8.00004C14.6673 4.31814 11.6825 1.33337 
8.00065 1.33337C4.31875 1.33337 1.33398 4.31814 1.33398 8.00004C1.33398 11.6819 4.31875 14.6667 8.00065 14.6667Z" stroke="currentColor" 
stroke-linecap="round" stroke-linejoin="round"></path><path d="M5.33464 8.00004C5.33464 11.6819 6.52854 14.6667 8.0013 14.6667C9.47406 14.6667 
10.668 11.6819 10.668 8.00004C10.668 4.31814 9.47406 1.33337 8.0013 1.33337C6.52854 1.33337 5.33464 4.31814 5.33464 8.00004Z" stroke="currentColor" 
stroke-linecap="round" stroke-linejoin="round"></path><path d="M1.33398 8H14.6673" stroke="currentColor" stroke-linecap="round" 
stroke-linejoin="round"></path></svg></div><span class="J9gHAG">English</span><svg viewBox="0 0 12 12" fill="none" width="12" height="12" 
color="currentColor"><path fill-rule="evenodd" clip-rule="evenodd" d="M6 8.146L11.146 3l.707.707-5.146 5.147a1 1 0 01-1.414 0L.146 3.707.854 3 6 
8.146z" fill="currentColor"></path></svg></div></div></div></li><li class="navbar__link navbar__link--tappable navbar__link--hoverable 
navbar__link--account"><div class="stardust-popover" id="stardust-popover1" tabindex="0"><div role="button" class="stardust-popover__target"><div 
class="navbar__link--account__container"><div class="shopee-avatar"><div class="shopee-avatar__placeholder"><svg enable-background="new 0 0 15 15" 
viewBox="0 0 15 15" x="0" y="0" class="shopee-svg-icon icon-headshot"><g><circle cx="7.5" cy="4.5" fill="none" r="3.8" 
stroke-miterlimit="10"></circle><path d="m1.5 14.2c0-3.3 2.7-6 6-6s6 2.7 6 6" fill="none" stroke-linecap="round" 
stroke-miterlimit="10"></path></g></svg></div><img class="shopee-avatar__img" 
src="https://down-my.img.susercontent.com/file/428e748e81ac2e111c8362b8ea5e92ad_tn"></div><div 
class="navbar__username">renalgy00</div></div></div></div></li></ul></nav></div></header><div class="X161pH"><div><div class="a11y-hidden" 
aria-live="polite"></div><h1 class="a11y-hidden">shopping cart</h1><section class="cart-page-header-wrapper container-wrapper"><div 
class="container"><div style="display: flex; align-items: center;"><div class="cart-page-header"><a class="cart-page-logo" href="/"><div></div><svg 
viewBox="0 0 192 65" class="shopee-svg-icon icon-shopee-logo"><g fill-rule="evenodd"><path d="M35.6717403 44.953764c-.3333497 2.7510509-2.0003116 
4.9543414-4.5823845 6.0575984-1.4379707.6145919-3.36871.9463856-4.896954.8421628-2.3840266-.0911143-4.6237865-.6708937-6.6883352-1.7307424-.7375522
-.3788551-1.8370513-1.1352759-2.6813095-1.8437757-.213839-.1790053-.239235-.2937577-.0977428-.4944671.0764015-.1151823.2172535-.3229831.5286218
-.7791994.45158-.6616533.5079208-.7446018.5587128-.8221779.14448-.2217688.3792333-.2411091.6107855-.0588804.0243289.0189105.0243289.0189105.0426824
.0333083.0379873.0294402.0379873.0294402.1276204.0990653.0907002.0706996.14448.1123887.166248.1287205 2.2265285 1.7438508 4.8196989 2.7495466 
7.4376251 2.8501162 3.6423042-.0496401 6.2615109-1.6873341 
6.7308041-4.2020035.5160305-2.7675977-1.6565047-5.1582742-5.9070334-6.4908212-1.329344-.4166762-4.6895175-1.7616869-5.3090528-2.1250697-2.9094471-1
.7071043-4.2697358-3.9430584-4.0763845-6.7048539.296216-3.8283059 3.8501677-6.6835796 8.340785-6.702705 2.0082079-.004083 4.0121475.4132378 
5.937338 1.2244562.6816382.2873109 1.8987274.9496089 2.3189359 
1.2633517.2420093.1777159.2898136.384872.1510957.60836-.0774686.12958-.2055158.3350171-.4754821.7632974l-.0029878.0047276c-.3553311.5640922
-.3664286.5817134-.447952.7136572-.140852.2144625-.3064598.2344475-.5604202.0732783-2.0600669-1.3839063-4.3437898-2.0801572-6.8554368-2.130442-3
.126914.061889-5.4706057 1.9228561-5.6246892 4.4579402-.0409751 2.2896772 1.676352 3.9613243 5.3858811 5.2358503 7.529819 2.4196871 10.4113092 
5.25648 9.869029 9.7292478M26.3725216 5.42669372c4.9022893 0 8.8982174 4.65220288 9.0851664 10.47578358H17.2875686c.186949-5.8235807 
4.1828771-10.47578358 9.084953-10.47578358m25.370857 11.57065968c0-.6047069-.4870064-1.0948761-1.0875481-1.0948761h-11.77736c-.28896-7.68927544-5
.7774923-13.82058185-12.5059489-13.82058185-6.7282432 0-12.2167755 6.13130641-12.5057355 
13.82058185l-11.79421958.0002149c-.59136492.0107446-1.06748731.4968309-1.06748731 1.0946612 0 
.0285807.00106706.0569465.00320118.0848825H.99995732l1.6812605 
37.0613963c.00021341.1031483.00405483.2071562.01173767.3118087.00170729.0236381.003628.0470614.00554871.0704847l.00362801.0782207.00405483.004083c
.25545428 2.5789222 2.12707837 4.6560709 4.67201764 4.7519129l.00576212.0055872h37.4122078c.0177132.0002149.0354264.0004298.0531396.0004298.0177132 
0 .0354264-.0002149.0531396-.0004298h.0796027l.0017073-.0015043c2.589329-.0706995 4.6867431-2.1768587 
4.9082648-4.787585l.0012805-.0012893.0017073-.0350275c.0021341-.0275062.0040548-.0547975.0057621-.0823037.0040548-.065757.0068292-.1312992.0078963
-.1964115l1.8344904-37.207738h-.0012805c.001067-.0186956.0014939-.0376062.0014939-.0565167M176.465457 41.1518926c.720839-2.3512494 
2.900423-3.9186779 5.443734-3.9186779 2.427686 0 4.739107 1.6486899 5.537598 3.9141989l.054826.1556978h-11.082664l.046506-.1512188zm13.50267 
3.4063683c.014933.0006399.014933.0006399.036906.0008531.021973-.0002132.021973-.0002132.044372-.0008531.53055-.0243144.950595-.4766911.950595-1
.0271786 0-.0266606-.000853-.0496953-.00256-.0865936.000427-.0068251.000427-.020262.000427-.0635588 
0-5.1926268-4.070748-9.4007319-9.09145-9.4007319-5.020488 0-9.091235 4.2081051-9.091235 9.4007319 0 .3871116.022399.7731567.067838 
1.1568557l.00256.0204753.01408.1013102c.250022 1.8683731 1.047233 3.5831812 2.306302 4.9708108-.00064-.0006399.00064.0006399.007253.0078915 
1.396026 1.536289 3.291455 2.5833031 5.393601 2.9748936l.02752.0053321v-.0027727l.13653.0228215c.070186.0119439.144211.0236746.243409.039031 
2.766879.332724 5.221231-.0661182 7.299484-1.1127057.511777-.2578611.971928-.5423827 
1.37064-.8429007.128211-.0968312.243622-.1904632.34346-.2781231.051412-.0452164.092372-.083181.114131-.1051493.468898-.4830897.498124-.6543572
.215249-1.0954297-.31146-.4956734-.586228-.9179769-.821744-1.2675504-.082345-.1224254-.154023-.2267215-.214396-.3133151-.033279-.0475624-.033279
-.0475624-.054399-.0776356-.008319-.0117306-.008319-.0117306-.013866-.0191956l-.00256-.0038391c-.256208-.3188605-.431565-.3480805-.715933-.0970445
-.030292.0268739-.131624.1051493-.14997.1245582-1.999321 1.775381-4.729508 2.3465571-7.455854 
1.7760208-.507724-.1362888-.982595-.3094759-1.419919-.5184948-1.708127-.8565509-2.918343-2.3826022-3.267563-4.1490253l-.02752-.1394881h13
.754612zM154.831964 41.1518926c.720831-2.3512494 2.900389-3.9186779 5.44367-3.9186779 2.427657 0 4.739052 1.6486899 5.537747 
3.9141989l.054612.1556978h-11.082534l.046505-.1512188zm13.502512 
3.4063683c.015146.0006399.015146.0006399.037118.0008531.02176-.0002132.02176-.0002132.044159-.0008531.530543-.0243144.950584-.4766911.950584-1
.0271786 0-.0266606-.000854-.0496953-.00256-.0865936.000426-.0068251.000426-.020262.000426-.0635588 
0-5.1926268-4.070699-9.4007319-9.091342-9.4007319-5.020217 0-9.091343 4.2081051-9.091343 9.4007319 0 .3871116.022826.7731567.068051 
1.1568557l.00256.0204753.01408.1013102c.250019 1.8683731 1.04722 3.5831812 2.306274 4.9708108-.00064-.0006399.00064.0006399.007254.0078915 1.396009 
1.536289 3.291417 2.5833031 5.393538 2.9748936l.027519.0053321v-.0027727l.136529.0228215c.070184.0119439.144209.0236746.243619.039031 
2.766847.332724 5.22117-.0661182 7.299185-1.1127057.511771-.2578611.971917-.5423827 
1.370624-.8429007.128209-.0968312.243619-.1904632.343456-.2781231.051412-.0452164.09237-.083181.11413-.1051493.468892-.4830897.498118-.6543572
.215246-1.0954297-.311457-.4956734-.586221-.9179769-.821734-1.2675504-.082344-.1224254-.154022-.2267215-.21418-.3133151-.033492-.0475624-.033492
-.0475624-.054612-.0776356-.008319-.0117306-.008319-.0117306-.013866-.0191956l-.002346-.0038391c-.256419-.3188605-.431774-.3480805-.716138-.0970445
-.030292.0268739-.131623.1051493-.149969.1245582-1.999084 1.775381-4.729452 2.3465571-7.455767 
1.7760208-.507717-.1362888-.982582-.3094759-1.419902-.5184948-1.708107-.8565509-2.918095-2.3826022-3.267311-4.1490253l-.027733-.1394881h13
.754451zM138.32144123 49.7357905c-3.38129629 0-6.14681004-2.6808521-6.23169343-6.04042014v-.31621743c.08401943-3.35418649 2.85039714-6.03546919 
6.23169343-6.03546919 3.44242097 0 6.23320537 2.7740599 6.23320537 6.1960534 0 3.42199346-2.7907844 6.19605336-6.23320537 
6.19605336m.00172791-15.67913203c-2.21776751 0-4.33682838.7553485-6.03989586 
2.140764l-.19352548.1573553V34.6208558c0-.4623792-.0993546-.56419733-.56740117-.56419733h-2.17651376c-.47409424 
0-.56761716.09428403-.56761716.56419733v27.6400724c0 .4539841.10583425.5641973.56761716.5641973h2.17651376c.46351081 0 
.56740117-.1078454.56740117-.5641973V50.734168l.19352548.1573553c1.70328347 1.3856307 3.82234434 2.1409792 6.03989586 2.1409792 5.27140956 0 
9.54473746-4.2479474 9.54473746-9.48802964 0-5.239867-4.2733279-9.48781439-9.54473746-9.48781439M115.907646 49.5240292c-3.449458 
0-6.245805-2.7496948-6.245805-6.1425854 0-3.3928907 2.79656-6.1427988 6.245805-6.1427988 3.448821 0 6.24538 2.7499081 6.24538 6.1427988 0 
3.3926772-2.796346 6.1425854-6.24538 6.1425854m.001914-15.5438312c-5.28187 0-9.563025 4.2112903-9.563025 9.4059406 0 5.1944369 4.281155 9.4059406 
9.563025 9.4059406 5.281657 0 9.562387-4.2115037 9.562387-9.4059406 0-5.1946503-4.280517-9.4059406-9.562387-9.4059406M94.5919049 
34.1890939c-1.9281307 0-3.7938902.6198995-5.3417715 1.7656047l-.188189.1393105V23.2574169c0-.4254677-.1395825-.5643476-.5649971-.5643476h-2
.2782698c-.4600414 0-.5652122.1100273-.5652122.5643476v29.2834155c0 .443339.1135587.5647782.5652122.5647782h2.2782698c.4226187 0 
.5649971-.1457701.5649971-.5647782v-9.5648406c.023658-3.011002 2.4931278-5.4412923 5.5299605-5.4412923 3.0445753 0 5.516841 2.4421328 5.5297454 
5.4630394v9.5430935c0 .4844647.0806524.5645628.5652122.5645628h2.2726775c.481764 0 
.565212-.0824666.565212-.5645628v-9.5710848c-.018066-4.8280677-4.0440197-8.7806537-8.9328471-8.7806537M62.8459442 
47.7938061l-.0053397.0081519c-.3248668.4921188-.4609221.6991347-.5369593.8179812-.2560916.3812097-.224267.551113.1668119.8816949.91266.7358184 
2.0858968 1.508535 2.8774525 1.8955369 2.2023021 1.076912 4.5810275 1.646045 7.1017886 1.6975309 1.6283921.0821628 3.6734936-.3050536 
5.1963734-.9842376 2.7569891-1.2298679 4.5131066-3.6269626 
4.8208863-6.5794607.4985136-4.7841067-2.6143125-7.7747902-10.6321784-10.1849709l-.0021359-.0006435c-3.7356476-1.2047686-5.4904836-2.8064071-5
.4911243-5.0426086.1099976-2.4715346 2.4015793-4.3179454 5.4932602-4.4331449 2.4904317.0062212 4.6923065.6675996 6.8557356 
2.0598624.4562232.2767364.666607.2256796.9733188-.172263.035242-.0587797.1332787-.2012238.543367-.790093l.0012815-.0019308c.3829626-.5500403
.5089793-.7336731.5403767-.7879478.258441-.4863266.2214903-.6738208-.244985-1.0046173-.459427-.3290803-1.7535544-1.0024722-2.4936356-1.2978721-2
.0583439-.8211991-4.1863175-1.2199998-6.3042524-1.1788111-4.8198184.1046878-8.578747 3.2393171-8.8265087 7.3515337-.1572005 2.9703036 1.350301 
5.3588174 4.5000778 7.124567.8829712.4661613 4.1115618 1.6865902 5.6184225 2.1278667 4.2847814 1.2547527 6.5186944 3.5630343 6.0571315 
6.2864205-.4192725 2.4743234-3.0117991 4.1199394-6.6498372 
4.2325647-2.6382344-.0549182-5.2963324-1.0217793-7.6043603-2.7562084-.0115337-.0083664-.0700567-.0519149-.1779185-.1323615-.1516472-.1130543
-.1516472-.1130543-.1742875-.1300017-.4705335-.3247898-.7473431-.2977598-1.0346184.1302162-.0346012.0529875-.3919333.5963776-.5681431.8632459
"></path></g></svg><div class="cart-page-logo__page-name">shopping cart</div></a></div><div class="cart-page-searchbar"><form role="search" 
autocomplete="off" class="shopee-searchbar"><div class="shopee-searchbar__main"><div class="shopee-searchbar-input"><input aria-label="Search for 
products, brands and shops" class="shopee-searchbar-input__input" maxlength="128" placeholder="Search for products, brands and shops" 
autocomplete="off" aria-autocomplete="list" aria-controls="shopee-searchbar-listbox" aria-expanded="false" role="combobox" 
value=""></div></div><button type="button" class="btn btn-solid-primary btn--s btn--inline shopee-searchbar__search-button"><svg height="19" 
viewBox="0 0 19 19" width="19" class="shopee-svg-icon"><g fill-rule="evenodd" stroke="none" stroke-width="1"><g transform="translate(-1016 
-32)"><g><g transform="translate(405 21)"><g transform="translate(611 11)"><path d="m8 16c4.418278 0 8-3.581722 8-8s-3.581722-8-8-8-8 3.581722-8 8 
3.581722 8 8 8zm0-2c-3.3137085 0-6-2.6862915-6-6s2.6862915-6 6-6 6 2.6862915 6 6-2.6862915 6-6 6z"></path><path d="m12.2972351 13.7114222 4.9799555 
4.919354c.3929077.3881263 1.0260608.3842503 1.4141871-.0086574.3881263-.3929076.3842503-1.0260607-.0086574-1.414187l-4.9799554-4.919354c-.3929077
-.3881263-1.0260608-.3842503-1.4141871.0086573-.3881263.3929077-.3842503 1.0260608.0086573 
1.4141871z"></path></g></g></g></g></g></svg></button></form></div></div></div></section><div class="tracking-impression-placeholder" 
style="position: fixed; z-index: 99999; bottom: 0px; left: 0px;"></div><div class="container"><main class="GO0LDV" style="margin-bottom: 0px;"><h2 
class="a11y-hidden">Product List Section</h2><div class="HLRhQB"><img width="20" height="20" 
src="https://deo.shopeemobile.com/shopee/shopee-pcmall-live-sg/cart/094f639ce7dff28ced5b.png" alt="fs-icon"><span class="UqssKR">Select free 
shipping voucher below to enjoy shipping discount</span></div><div class="Za1N64"><div class="SQGY8I"><label class="stardust-checkbox"><input 
class="stardust-checkbox__input" type="checkbox" aria-checked="false" aria-disabled="false" tabindex="0" role="checkbox" aria-label="Click here to 
select all products"><div class="stardust-checkbox__box"></div></label></div><div class="jX4z5R">Product</div><div class="jHcdvj">Unit 
Price</div><div class="o1QlcH">Quantity</div><div class="RT5qRd">Total Price</div><div class="TkKRaF">Actions</div></div><section 
class="AuhAvM"><h3 class="a11y-hidden">Shop Section</h3><div class="JsC6Oq NWPcV8"><div class="gzSvrb"><div class="Ll5dDW"><label 
class="stardust-checkbox"><input class="stardust-checkbox__input" type="checkbox" aria-checked="false" tabindex="0" role="checkbox" 
aria-label="Click here to select all products in Miracolo Mall"><div class="stardust-checkbox__box"></div></label></div><a class="QcqMX5" 
href="/miracolo.co?categoryId=100637&amp;entryPoint=cart&amp;itemId=13413660973"><div class="Koi0Pw"><svg xmlns="http://www.w3.org/2000/svg" 
width="58" height="16" fill="none"><title>Preferred Seller</title><path fill="#EE4D2D" fill-rule="evenodd" d="M0 2C0 .9.9 0 2 0h54a2 2 0 012 2v12a2 
2 0 01-2 2H2a2 2 0 01-2-2V2z" clip-rule="evenodd"></path><path fill="#fff" d="M6.3 9.3v3.2H5V4H8c1 0 1.7.2 2.3.7.6.5.8 1.2.8 2s-.2 1.5-.8 
2c-.5.4-1.3.6-2.3.6H6.3zm0-1.2h1.8c.6 0 1 0 1.2-.3.3-.3.5-.6.5-1.1 0-.5-.2-.8-.5-1.1-.2-.3-.6-.4-1.1-.4H6.3v3zm9.4-.6h-.6c-.6 0-1 
.2-1.3.7v4.3h-1.4V6.2h1.4v.7c.3-.6.8-.9 1.4-.9l.5.1v1.4zm3.6 5.1a3 3 0 01-2.2-.8c-.6-.6-.8-1.4-.8-2.3v-.2c0-.6 0-1.2.3-1.7s.6-.9 1-1.1c.5-.3 1-.5 
1.5-.5.9 0 1.6.3 2 .9.5.5.7 1.3.7 2.3v.6h-4.1c0 .5.2 1 .5 1.2.3.3.7.5 1.2.5a2 2 0 001.6-.8l.7.7c-.2.4-.6.7-1 1l-1.4.2zm-.2-5.4c-.4 0-.7.1-1 .4l-.4 
1.1h2.7c0-.5-.1-.9-.3-1.1-.3-.3-.6-.4-1-.4zm4.4 5.3V7.2h-1v-1h1v-.6c0-.7.1-1.3.5-1.6.4-.4 1-.6 1.7-.6h.8v1.2h-.6c-.7 0-1 .3-1 
1v.6h1.3v1h-1.3v5.3h-1.4zm6.4.1a3 3 0 01-2.2-.8c-.6-.6-.9-1.4-.9-2.3v-.2c0-.6.1-1.2.4-1.7.2-.5.6-.9 1-1.1.5-.3 1-.5 1.5-.5.9 0 1.5.3 2 .9.5.5.7 
1.3.7 2.3v.6h-4.1c0 .5.2 1 .5 1.2.3.3.7.5 1.1.5a2 2 0 001.6-.8l.8.7-1 1-1.4.2zm-.2-5.4c-.4 0-.7.1-1 .4-.2.3-.4.7-.4 
1.1H31c0-.5-.2-.9-.4-1.1-.2-.3-.5-.4-1-.4zm7.1.3h-.5c-.7 0-1.1.2-1.4.7v4.3h-1.4V6.2H35v.7c.3-.6.8-.9 1.4-.9l.5.1v1.4zm4.2 0h-.5c-.7 
0-1.1.2-1.3.7v4.3h-1.5V6.2h1.4v.7c.4-.6.8-.9 1.5-.9l.5.1v1.4zm3.6 5.1a3 3 0 01-2.2-.8c-.5-.6-.8-1.4-.8-2.3v-.2c0-.6.1-1.2.4-1.7.2-.5.5-.9 
1-1.1.4-.3 1-.5 1.5-.5.8 0 1.5.3 2 .9.4.5.7 1.3.7 2.3v.6H43c0 .5.2 1 .5 1.2.4.3.7.5 1.2.5a2 2 0 001.6-.8l.8.7-1 1-1.5.2zm-.1-5.4c-.4 0-.8.1-1 .4L43 
8.7h2.8c0-.5-.2-.9-.4-1.1-.2-.3-.6-.4-1-.4zm3.5 2c0-.9.2-1.7.7-2.3.4-.6 1-.9 1.8-.9a2 2 0 011.6.7V3.5h1.5v9h-1.3v-.7c-.5.6-1 .8-1.8.8-.7 
0-1.3-.3-1.8-.9a4 4 0 01-.7-2.4zm1.4.2c0 .7.2 1.2.4 1.5.3.4.6.6 1 .6.6 0 1-.3 1.3-.8V8c-.2-.5-.6-.8-1.2-.8-.5 0-.8.2-1 .6a3 3 0 00-.5 
1.6z"></path></svg></div><span style="margin-left: 10px;">Miracolo Mall</span></a><button class="Eg4UEE"><svg viewBox="0 0 16 16" 
class="shopee-svg-icon AxeMgG"><g fill-rule="evenodd"><path d="M15 4a1 1 0 01.993.883L16 5v9.932a.5.5 0 01-.82.385l-2.061-1.718-8.199.001a1 1 0 
01-.98-.8l-.016-.117-.108-1.284 8.058.001a2 2 0 001.976-1.692l.018-.155L14.293 4H15zm-2.48-4a1 1 0 011 1l-.003.077-.646 8.4a1 1 0 
01-.997.923l-8.994-.001-2.06 1.718a.5.5 0 01-.233.108l-.087.007a.5.5 0 01-.492-.41L0 11.732V1a1 1 0 011-1h11.52zM3.646 4.246a.5.5 0 000 
.708c.305.304.694.526 1.146.682A4.936 4.936 0 006.4 5.9c.464 0 1.02-.062 1.608-.264.452-.156.841-.378 1.146-.682a.5.5 0 
10-.708-.708c-.185.186-.445.335-.764.444a4.004 4.004 0 01-2.564 0c-.319-.11-.579-.258-.764-.444a.5.5 0 00-.708 0z"></path></g></svg></button><div 
class="cVlPY7"></div><div class="p1DEnN"><svg fill="none" viewBox="0 0 18 18" class="shopee-svg-icon KeOYUq icon-coin-line"><path stroke="#FFA600" 
stroke-width="1.3" d="M17.35 9A8.35 8.35 0 11.65 9a8.35 8.35 0 0116.7 0z"></path><path fill="#FFA600" fill-rule="evenodd" stroke="#FFA600" 
stroke-width=".2" d="M6.86 4.723c-.683.576-.998 1.627-.75 2.464.215.725.85 1.258 1.522 1.608.37.193.77.355 
1.177.463.1.027.2.051.3.08.098.03.196.062.294.096.06.021.121.044.182.067.017.006.107.041.04.014-.07-.028.071.03.087.037.286.124.56.27.82.44.114.076
.045.024.151.111a2.942 2.942 0 01.322.303c.087.093.046.042.114.146.18.275.245.478.235.8-.01.328-.14.659-.325.867-.47.53-1.232.73-1.934.696a4.727 
4.727 0 01-1.487-.307c-.45-.182-.852-.462-1.242-.737-.25-.176-.643-.04-.788.197-.17.279-.044.574.207.75.753.532 1.539.946 2.474 1.098.885.144 
1.731.124 2.563-.224.78-.326 1.416-.966 1.607-1.772.198-.838-.023-1.644-.61-2.29-.683-.753-1.722-1.17-2.706-1.43a4.563 4.563 0 
01-.543-.183c.122.048-.044-.02-.078-.035a4.77 4.77 0 01-.422-.212c-.594-.338-.955-.722-.872-1.369.105-.816.757-1.221 1.555-1.28.808-.06 1.648.135 
2.297.554.614.398 1.19-.553.58-.947-1.33-.86-3.504-1.074-4.77-.005z" clip-rule="evenodd"></path></svg>Shopee coins 
redeemable</div></div></div><section class="RqMReY" role="list"><div class="_9G37m"><div class="wsVAKH"><span class="lKqYHD">Free 
Gift</span><span>Spend RM10.00 to get 5 free gifts</span><span class="Vm8iNU"><a 
href="/purchase-with-gifts/158969830379719/13413660973/514827991?showGifts=0">Add more<svg viewBox="0 0 12 12" fill="none" width="12" height="12" 
color="#ee4d2d" class="MuMxsb"><path fill-rule="evenodd" clip-rule="evenodd" d="M9.293 6L4.146.854l.708-.708L10 5.293a1 1 0 010 1.414l-5.146 
5.147-.708-.707L9.293 6z" fill="currentColor"></path></svg></a></span></div><div class="lDiGJB kEMRam" role="listitem"><h4 
class="a11y-hidden">cart_accessibility_item</h4><div class="f1bSN6"><div class="Xp4RLg"><label class="stardust-checkbox"><input 
class="stardust-checkbox__input" type="checkbox" aria-checked="false" aria-disabled="false" tabindex="0" role="checkbox" aria-label="Click here to 
select this product"><div class="stardust-checkbox__box"></div></label></div><div class="brf29Y"><div class="bzhajK"><a title="MIRA  [5KGx2] 10kg 
Set Hexagon Premium Dumbbell Dumbells Sport Gym Fitness Exercise Weight Training Equipment 哑铃 健身" 
href="/MIRA-5KGx2-10kg-Set-Hexagon-Premium-Dumbbell-Dumbells-Sport-Gym-Fitness-Exercise-Weight-Training-Equipment-哑铃-健身-i.514827991.13413660973
?xptdk=966d0de3-0c45-425c-9318-97c1b574c6f8"><img class="jFEiVQ" src="https://down-my.img.susercontent.com/file/3fa8ed768dd7ad80a04895fe3989332f" 
alt="product image"></a><div class="Ou_0WX"><a class="c54pg1" title="MIRA  [5KGx2] 10kg Set Hexagon Premium Dumbbell Dumbells Sport Gym Fitness 
Exercise Weight Training Equipment 哑铃 健身" href="/MIRA-5KGx2-10kg-Set-Hexagon-Premium-Dumbbell-Dumbells-Sport-Gym-Fitness-Exercise-Weight-Training
-Equipment-哑铃-健身-i.514827991.13413660973?xptdk=966d0de3-0c45-425c-9318-97c1b574c6f8">MIRA  [5KGx2] 10kg Set Hexagon Premium Dumbbell Dumbells Sport 
Gym Fitness Exercise Weight Training Equipment 哑铃 健身</a><img class="Kv1AvK" 
src="https://down-my.img.susercontent.com/file/my-50009109-07d26479b71d36d840c404c716d03602"><div class="gvFc9h"></div></div></div></div><div 
class="eHDC_o"><div class="qNRZqG"><button class="mM4TZ8" role="button" tabindex="0"><div class="iIg1CN">Variations:<div 
class="E33rwr"></div></div><div class="dDPSp3">5 KG x 2 pcs 【10KG】</div></button><div></div></div></div><div class="gJyWia"><div><span 
class="vjkBXu tnTSPU">RM70.00</span><span class="vjkBXu">RM36.80</span></div></div><div class="sluy3i"><div class="GpmJtT 
shopee-input-quantity"><button class="WNSVcC" aria-label="Decrease"><svg enable-background="new 0 0 10 10" viewBox="0 0 10 10" x="0" y="0" 
class="shopee-svg-icon"><polygon points="4.5 4.5 3.5 4.5 0 4.5 0 5.5 3.5 5.5 4.5 5.5 10 5.5 10 4.5"></polygon></svg></button><input class="WNSVcC 
g2m9n4" type="text" role="spinbutton" aria-valuenow="1" value="1"><button class="WNSVcC" aria-label="Increase"><svg enable-background="new 0 0 10 
10" viewBox="0 0 10 10" x="0" y="0" class="shopee-svg-icon icon-plus-sign"><polygon points="10 4.5 5.5 4.5 5.5 0 4.5 0 4.5 4.5 0 4.5 0 5.5 4.5 5.5 
4.5 10 5.5 10 5.5 5.5 10 5.5"></polygon></svg></button></div></div><div class="HRvCAv"><span>RM36.80</span><span class="a11y-hidden">Total price: 
RM36.80</span></div><div class="bRSn43 TvSDdG"><button class="lSrQtj">Delete</button><div class="J8cCGR"><button class="shopee-button-no-outline 
slfWNx"><span class="wZrjgF">Find Similar</span><svg enable-background="new 0 0 15 15" viewBox="0 0 15 15" x="0" y="0" class="shopee-svg-icon 
f3N1Rf icon-down-arrow-filled"><path d="m6.5 12.9-6-7.9s-1.4-1.5.5-1.5h13s1.8 0 .6 1.5l-6 7.9c-.1 0-.9 1.3-2.1 
0z"></path></svg></button></div></div></div></div><div class="t89ViJ"></div></div></section><div class="_RPX38"><img width="20" height="20" 
src="https://deo.shopeemobile.com/shopee/shopee-pcmall-live-sg/cart/094f639ce7dff28ced5b.png" alt="fs-icon"><div class="Cmb29y">Up to RM5.00 off 
shipping for orders over RM0.00</div><div class="shopee-drawer" id="pc-drawer-id-0" tabindex="0"><span class="Eb1Wor" 
aria-describedby="514827991_shipping_discount"> Learn more </span></div></div></section><section class="AuhAvM"><h3 class="a11y-hidden">Shop 
Section</h3><div class="JsC6Oq"><div class="gzSvrb"><div class="Ll5dDW"><label class="stardust-checkbox"><input class="stardust-checkbox__input" 
type="checkbox" aria-checked="false" tabindex="0" role="checkbox" aria-label="Click here to select all products in 3H Fitness"><div 
class="stardust-checkbox__box"></div></label></div><a class="QcqMX5" 
href="/3hfitness21?categoryId=100637&amp;entryPoint=cart&amp;itemId=21989843317"><div><svg width="17" height="16" viewBox="0 0 17 16" 
class="Koi0Pw"><title>Shop Icon</title><path d="M1.95 6.6c.156.804.7 1.867 1.357 1.867.654 0 1.43 0 1.43-.933h.932s0 .933 1.155.933c1.176 0 
1.15-.933 1.15-.933h.984s-.027.933 1.148.933c1.157 0 1.15-.933 1.15-.933h.94s0 .933 1.43.933c1.368 0 1.356-1.867 
1.356-1.867H1.95zm11.49-4.666H3.493L2.248 5.667h12.437L13.44 1.934zM2.853 14.066h11.22l-.01-4.782c-.148.02-.295.042-.465.042-.7 
0-1.436-.324-1.866-.86-.376.53-.88.86-1.622.86-.667 0-1.255-.417-1.64-.86-.39.443-.976.86-1.643.86-.74 
0-1.246-.33-1.623-.86-.43.536-1.195.86-1.895.86-.152 0-.297-.02-.436-.05l-.018 4.79zM14.996 12.2v.933L14.984 15H1.94l-.002-1.867V8.84C1.355 8.306 
1.003 7.456 1 6.6L2.87 1h11.193l1.866 5.6c0 .943-.225 1.876-.934 2.39v3.21z" stroke-width=".3" stroke="#333" fill="#333" 
fill-rule="evenodd"></path></svg></div><span style="margin-left: 10px;">3H Fitness</span></a><button class="Eg4UEE"><svg viewBox="0 0 16 16" 
class="shopee-svg-icon AxeMgG"><g fill-rule="evenodd"><path d="M15 4a1 1 0 01.993.883L16 5v9.932a.5.5 0 01-.82.385l-2.061-1.718-8.199.001a1 1 0 
01-.98-.8l-.016-.117-.108-1.284 8.058.001a2 2 0 001.976-1.692l.018-.155L14.293 4H15zm-2.48-4a1 1 0 011 1l-.003.077-.646 8.4a1 1 0 
01-.997.923l-8.994-.001-2.06 1.718a.5.5 0 01-.233.108l-.087.007a.5.5 0 01-.492-.41L0 11.732V1a1 1 0 011-1h11.52zM3.646 4.246a.5.5 0 000 
.708c.305.304.694.526 1.146.682A4.936 4.936 0 006.4 5.9c.464 0 1.02-.062 1.608-.264.452-.156.841-.378 1.146-.682a.5.5 0 
10-.708-.708c-.185.186-.445.335-.764.444a4.004 4.004 0 01-2.564 0c-.319-.11-.579-.258-.764-.444a.5.5 0 00-.708 0z"></path></g></svg></button><div 
class="cVlPY7"></div></div></div><section class="RqMReY" role="list"><div class="lDiGJB" role="listitem"><h4 
class="a11y-hidden">cart_accessibility_item</h4><div class="f1bSN6"><div class="Xp4RLg"><label class="stardust-checkbox"><input 
class="stardust-checkbox__input" type="checkbox" aria-checked="false" aria-disabled="false" tabindex="0" role="checkbox" aria-label="Click here to 
select this product"><div class="stardust-checkbox__box"></div></label></div><div class="brf29Y"><div class="bzhajK"><a title="3H [
1/1.5/2.0/2.5/3/4/5]KG Lady's Dumbbell Hexagon Dumbbell Gym Fitness Exercise Home Weight Training Workout Dumbell" 
href="/3H-1-1.5-2.0-2.5-3-4-5-KG-Lady's-Dumbbell-Hexagon-Dumbbell-Gym-Fitness-Exercise-Home-Weight-Training-Workout-Dumbell-i.544815642.21989843317
?xptdk=e560ec8d-d943-44d0-95d4-7c9ac3812694"><img class="jFEiVQ" src="https://down-my.img.susercontent.com/file/my-11134207-7qul8-lhzwhqy9gfdp41" 
alt="product image"></a><div class="Ou_0WX"><a class="c54pg1" title="3H [1/1.5/2.0/2.5/3/4/5]KG Lady's Dumbbell Hexagon Dumbbell Gym Fitness 
Exercise Home Weight Training Workout Dumbell" href="/3H-1-1.5-2.0-2.5-3-4-5-KG-Lady's-Dumbbell-Hexagon-Dumbbell-Gym-Fitness-Exercise-Home-Weight
-Training-Workout-Dumbell-i.544815642.21989843317?xptdk=e560ec8d-d943-44d0-95d4-7c9ac3812694">3H [1/1.5/2.0/2.5/3/4/5]KG Lady's Dumbbell Hexagon 
Dumbbell Gym Fitness Exercise Home Weight Training Workout Dumbell</a><img class="Kv1AvK" 
src="https://down-my.img.susercontent.com/file/my-50009109-07d26479b71d36d840c404c716d03602"><div class="gvFc9h"></div></div></div><div 
class="Jkd76v bzhajK">RM 22.21 on 25 Feb Only</div></div><div class="eHDC_o"><div class="qNRZqG"><button class="mM4TZ8" role="button" 
tabindex="0"><div class="iIg1CN">Variations:<div class="E33rwr"></div></div><div 
class="dDPSp3">3.0kg-Blue</div></button><div></div></div></div><div class="gJyWia"><div><span class="vjkBXu">RM23.15</span></div></div><div 
class="sluy3i"><div class="GpmJtT shopee-input-quantity"><button class="WNSVcC" aria-label="Decrease"><svg enable-background="new 0 0 10 10" 
viewBox="0 0 10 10" x="0" y="0" class="shopee-svg-icon"><polygon points="4.5 4.5 3.5 4.5 0 4.5 0 5.5 3.5 5.5 4.5 5.5 10 5.5 10 
4.5"></polygon></svg></button><input class="WNSVcC g2m9n4" type="text" role="spinbutton" aria-valuenow="1" value="1"><button class="WNSVcC" 
aria-label="Increase"><svg enable-background="new 0 0 10 10" viewBox="0 0 10 10" x="0" y="0" class="shopee-svg-icon icon-plus-sign"><polygon 
points="10 4.5 5.5 4.5 5.5 0 4.5 0 4.5 4.5 0 4.5 0 5.5 4.5 5.5 4.5 10 5.5 10 5.5 5.5 10 5.5"></polygon></svg></button></div></div><div 
class="HRvCAv"><span>RM23.15</span><span class="a11y-hidden">Total price: RM23.15</span></div><div class="bRSn43 TvSDdG"><button 
class="lSrQtj">Delete</button><div class="J8cCGR"><button class="shopee-button-no-outline slfWNx"><span class="wZrjgF">Find Similar</span><svg 
enable-background="new 0 0 15 15" viewBox="0 0 15 15" x="0" y="0" class="shopee-svg-icon f3N1Rf icon-down-arrow-filled"><path d="m6.5 
12.9-6-7.9s-1.4-1.5.5-1.5h13s1.8 0 .6 1.5l-6 7.9c-.1 0-.9 1.3-2.1 0z"></path></svg></button></div></div></div></div><div class="RIfxP9"></div><div 
class="lDiGJB" role="listitem"><h4 class="a11y-hidden">cart_accessibility_item</h4><div class="f1bSN6"><div class="Xp4RLg"><label 
class="stardust-checkbox"><input class="stardust-checkbox__input" type="checkbox" aria-checked="false" aria-disabled="false" tabindex="0" 
role="checkbox" aria-label="Click here to select this product"><div class="stardust-checkbox__box"></div></label></div><div class="brf29Y"><div 
class="bzhajK"><a title="3H [2/4/6/8/10]kg Kettlebell/ [2*(2.5/5.0)KG] Hexagon Dumbbell/Dumbbell Plate For Weight Lifting Gym Training Home" 
href="/3H-2-4-6-8-10-kg-Kettlebell-2*(2.5-5.0)KG-Hexagon-Dumbbell-Dumbbell-Plate-For-Weight-Lifting-Gym-Training-Home-i.544815642.18616076823?xptdk
=c82c52cb-ffd0-43e2-884b-7af51addec42"><img class="jFEiVQ" src="https://down-my.img.susercontent.com/file/my-11134207-7qul5-lhykc142l90d37" 
alt="product image"></a><div class="Ou_0WX"><a class="c54pg1" title="3H [2/4/6/8/10]kg Kettlebell/ [2*(2.5/5.0)KG] Hexagon Dumbbell/Dumbbell Plate 
For Weight Lifting Gym Training Home" href="/3H-2-4-6-8-10-kg-Kettlebell-2*(
2.5-5.0)KG-Hexagon-Dumbbell-Dumbbell-Plate-For-Weight-Lifting-Gym-Training-Home-i.544815642.18616076823?xptdk=c82c52cb-ffd0-43e2-884b-7af51addec42
">3H [2/4/6/8/10]kg Kettlebell/ [2*(2.5/5.0)KG] Hexagon Dumbbell/Dumbbell Plate For Weight Lifting Gym Training Home</a><img class="Kv1AvK" 
src="https://down-my.img.susercontent.com/file/my-50009109-07d26479b71d36d840c404c716d03602"><div class="gvFc9h"></div></div></div><div 
class="Jkd76v bzhajK">RM 19.90 on 25 Feb Only</div></div><div class="eHDC_o"><div class="qNRZqG"><button class="mM4TZ8" role="button" 
tabindex="0"><div class="iIg1CN">Variations:<div class="E33rwr"></div></div><div class="dDPSp3">2.5KG X2 
Dumbbell</div></button><div></div></div></div><div class="gJyWia"><div><span class="vjkBXu">RM19.90</span></div></div><div class="sluy3i"><div 
class="GpmJtT shopee-input-quantity"><button class="WNSVcC" aria-label="Decrease"><svg enable-background="new 0 0 10 10" viewBox="0 0 10 10" x="0" 
y="0" class="shopee-svg-icon"><polygon points="4.5 4.5 3.5 4.5 0 4.5 0 5.5 3.5 5.5 4.5 5.5 10 5.5 10 4.5"></polygon></svg></button><input 
class="WNSVcC g2m9n4" type="text" role="spinbutton" aria-valuenow="1" value="1"><button class="WNSVcC" aria-label="Increase"><svg 
enable-background="new 0 0 10 10" viewBox="0 0 10 10" x="0" y="0" class="shopee-svg-icon icon-plus-sign"><polygon points="10 4.5 5.5 4.5 5.5 0 4.5 
0 4.5 4.5 0 4.5 0 5.5 4.5 5.5 4.5 10 5.5 10 5.5 5.5 10 5.5"></polygon></svg></button></div></div><div class="HRvCAv"><span>RM19.90</span><span 
class="a11y-hidden">Total price: RM19.90</span></div><div class="bRSn43 TvSDdG"><button class="lSrQtj">Delete</button><div class="J8cCGR"><button 
class="shopee-button-no-outline slfWNx"><span class="wZrjgF">Find Similar</span><svg enable-background="new 0 0 15 15" viewBox="0 0 15 15" x="0" 
y="0" class="shopee-svg-icon f3N1Rf icon-down-arrow-filled"><path d="m6.5 12.9-6-7.9s-1.4-1.5.5-1.5h13s1.8 0 .6 1.5l-6 7.9c-.1 0-.9 1.3-2.1 
0z"></path></svg></button></div></div></div></div><div class="RIfxP9"></div><div class="lDiGJB" role="listitem"><h4 
class="a11y-hidden">cart_accessibility_item</h4><div class="f1bSN6"><div class="Xp4RLg"><label class="stardust-checkbox"><input 
class="stardust-checkbox__input" type="checkbox" aria-checked="false" aria-disabled="false" tabindex="0" role="checkbox" aria-label="Click here to 
select this product"><div class="stardust-checkbox__box"></div></label></div><div class="brf29Y"><div class="bzhajK"><a title="3H [2/4/6/8/10]kg 
Kettlebell/ [2*(2.5/5.0)KG] Hexagon Dumbbell/Dumbbell Plate For Weight Lifting Gym Training Home" href="/3H-2-4-6-8-10-kg-Kettlebell-2*(
2.5-5.0)KG-Hexagon-Dumbbell-Dumbbell-Plate-For-Weight-Lifting-Gym-Training-Home-i.544815642.18616076823?xptdk=875d7ea4-7875-4bf0-a089-32ee88cb0fa3
"><img class="jFEiVQ" src="https://down-my.img.susercontent.com/file/sg-11134201-22110-sq2yzl1u3wjv64" alt="product image"></a><div 
class="Ou_0WX"><a class="c54pg1" title="3H [2/4/6/8/10]kg Kettlebell/ [2*(2.5/5.0)KG] Hexagon Dumbbell/Dumbbell Plate For Weight Lifting Gym 
Training Home" href="/3H-2-4-6-8-10-kg-Kettlebell-2*(2.5-5.0)KG-Hexagon-Dumbbell-Dumbbell-Plate-For-Weight-Lifting-Gym-Training-Home-i.544815642
.18616076823?xptdk=875d7ea4-7875-4bf0-a089-32ee88cb0fa3">3H [2/4/6/8/10]kg Kettlebell/ [2*(2.5/5.0)KG] Hexagon Dumbbell/Dumbbell Plate For Weight 
Lifting Gym Training Home</a><img class="Kv1AvK" src="https://down-my.img.susercontent.com/file/my-50009109-07d26479b71d36d840c404c716d03602"><div 
class="gvFc9h"></div></div></div><div class="Jkd76v bzhajK">RM 36.50 on 25 Feb Only</div></div><div class="eHDC_o"><div class="qNRZqG"><button 
class="mM4TZ8" role="button" tabindex="0"><div class="iIg1CN">Variations:<div class="E33rwr"></div></div><div class="dDPSp3">5.0KG X2 
Dumbbell</div></button><div></div></div></div><div class="gJyWia"><div><span class="vjkBXu">RM36.50</span></div></div><div class="sluy3i"><div 
class="GpmJtT shopee-input-quantity"><button class="WNSVcC" aria-label="Decrease"><svg enable-background="new 0 0 10 10" viewBox="0 0 10 10" x="0" 
y="0" class="shopee-svg-icon"><polygon points="4.5 4.5 3.5 4.5 0 4.5 0 5.5 3.5 5.5 4.5 5.5 10 5.5 10 4.5"></polygon></svg></button><input 
class="WNSVcC g2m9n4" type="text" role="spinbutton" aria-valuenow="1" value="1"><button class="WNSVcC" aria-label="Increase"><svg 
enable-background="new 0 0 10 10" viewBox="0 0 10 10" x="0" y="0" class="shopee-svg-icon icon-plus-sign"><polygon points="10 4.5 5.5 4.5 5.5 0 4.5 
0 4.5 4.5 0 4.5 0 5.5 4.5 5.5 4.5 10 5.5 10 5.5 5.5 10 5.5"></polygon></svg></button></div></div><div class="HRvCAv"><span>RM36.50</span><span 
class="a11y-hidden">Total price: RM36.50</span></div><div class="bRSn43 TvSDdG"><button class="lSrQtj">Delete</button><div class="J8cCGR"><button 
class="shopee-button-no-outline slfWNx"><span class="wZrjgF">Find Similar</span><svg enable-background="new 0 0 15 15" viewBox="0 0 15 15" x="0" 
y="0" class="shopee-svg-icon f3N1Rf icon-down-arrow-filled"><path d="m6.5 12.9-6-7.9s-1.4-1.5.5-1.5h13s1.8 0 .6 1.5l-6 7.9c-.1 0-.9 1.3-2.1 
0z"></path></svg></button></div></div></div></div></section><div class="ArX7yj"><svg fill="none" viewBox="0 -2 23 22" class="shopee-svg-icon lGPe96 
icon-voucher-line"><g filter="url(#voucher-filter0_d)"><mask id="a" fill="#fff"><path fill-rule="evenodd" clip-rule="evenodd" d="M1 2h18v2.32a1.5 
1.5 0 000 2.75v.65a1.5 1.5 0 000 2.75v.65a1.5 1.5 0 000 2.75V16H1v-2.12a1.5 1.5 0 000-2.75v-.65a1.5 1.5 0 000-2.75v-.65a1.5 1.5 0 
000-2.75V2z"></path></mask><path d="M19 2h1V1h-1v1zM1 2V1H0v1h1zm18 2.32l.4.92.6-.26v-.66h-1zm0 2.75h1v-.65l-.6-.26-.4.91zm0 
.65l.4.92.6-.26v-.66h-1zm0 2.75h1v-.65l-.6-.26-.4.91zm0 .65l.4.92.6-.26v-.66h-1zm0 2.75h1v-.65l-.6-.26-.4.91zM19 16v1h1v-1h-1zM1 
16H0v1h1v-1zm0-2.12l-.4-.92-.6.26v.66h1zm0-2.75H0v.65l.6.26.4-.91zm0-.65l-.4-.92-.6.26v.66h1zm0-2.75H0v.65l.6.26.4-.91zm0-.65l-.4-.92-.6.26v
.66h1zm0-2.75H0v.65l.6.26.4-.91zM19 1H1v2h18V1zm1 3.32V2h-2v2.32h2zm-.9 1.38c0-.2.12-.38.3-.46l-.8-1.83a2.5 2.5 0 00-1.5 2.29h2zm.3.46a.5.5 0 
01-.3-.46h-2c0 1.03.62 1.9 1.5 2.3l.8-1.84zm.6 1.56v-.65h-2v.65h2zm-.9 1.38c0-.2.12-.38.3-.46l-.8-1.83a2.5 2.5 0 00-1.5 2.29h2zm.3.46a.5.5 0 
01-.3-.46h-2c0 1.03.62 1.9 1.5 2.3l.8-1.84zm.6 1.56v-.65h-2v.65h2zm-.9 1.38c0-.2.12-.38.3-.46l-.8-1.83a2.5 2.5 0 00-1.5 2.29h2zm.3.46a.5.5 0 
01-.3-.46h-2c0 1.03.62 1.9 1.5 2.3l.8-1.84zM20 16v-2.13h-2V16h2zM1 17h18v-2H1v2zm-1-3.12V16h2v-2.12H0zm1.4.91a2.5 2.5 0 001.5-2.29h-2a.5.5 0 
01-.3.46l.8 1.83zm1.5-2.29a2.5 2.5 0 00-1.5-2.3l-.8 1.84c.18.08.3.26.3.46h2zM0 10.48v.65h2v-.65H0zM.9 9.1a.5.5 0 01-.3.46l.8 1.83A2.5 2.5 0 002.9 
9.1h-2zm-.3-.46c.18.08.3.26.3.46h2a2.5 2.5 0 00-1.5-2.3L.6 8.65zM0 7.08v.65h2v-.65H0zM.9 5.7a.5.5 0 01-.3.46l.8 1.83A2.5 2.5 0 002.9 
5.7h-2zm-.3-.46c.18.08.3.26.3.46h2a2.5 2.5 0 00-1.5-2.3L.6 5.25zM0 2v2.33h2V2H0z" mask="url(#a)"></path></g><path clip-rule="evenodd" d="M6.49 
14.18h.86v-1.6h-.86v1.6zM6.49 11.18h.86v-1.6h-.86v1.6zM6.49 8.18h.86v-1.6h-.86v1.6zM6.49 5.18h.86v-1.6h-.86v1.6z"></path><defs><filter 
id="voucher-filter0_d" x="0" y="1" width="20" height="16" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB"><feFlood 
flood-opacity="0" result="BackgroundImageFix"></feFlood><feColorMatrix in="SourceAlpha" values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 127 
0"></feColorMatrix><feOffset></feOffset><feGaussianBlur stdDeviation=".5"></feGaussianBlur><feColorMatrix values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
0 0.09 0"></feColorMatrix><feBlend in2="BackgroundImageFix" result="effect1_dropShadow"></feBlend><feBlend in="SourceGraphic" 
in2="effect1_dropShadow" result="shape"></feBlend></filter></defs></svg><div class="N9nCmB"><div class="nKTIzW">View all shop vouchers</div><div 
class="JC72Dv"><button class="qe2YoR">More Vouchers</button><div style="display: contents;"></div></div></div></div><div class="_RPX38"><img 
width="20" height="20" src="https://deo.shopeemobile.com/shopee/shopee-pcmall-live-sg/cart/094f639ce7dff28ced5b.png" alt="fs-icon"><div 
class="Cmb29y">Up to RM5.00 off shipping for orders over RM0.00</div><div class="shopee-drawer" id="pc-drawer-id-1" tabindex="0"><span 
class="Eb1Wor" aria-describedby="544815642_shipping_discount"> Learn more </span></div></div></section><section class="AuhAvM"><h3 
class="a11y-hidden">Shop Section</h3><div class="JsC6Oq"><div class="gzSvrb"><div class="Ll5dDW"><label class="stardust-checkbox"><input 
class="stardust-checkbox__input" type="checkbox" aria-checked="false" tabindex="0" role="checkbox" aria-label="Click here to select all products in 
Sonala.my"><div class="stardust-checkbox__box"></div></label></div><a class="QcqMX5" 
href="/sonala.my?categoryId=100637&amp;entryPoint=cart&amp;itemId=25951007347"><div class="Koi0Pw"><svg xmlns="http://www.w3.org/2000/svg" 
width="58" height="16" fill="none"><title>Preferred Seller</title><path fill="#EE4D2D" fill-rule="evenodd" d="M0 2C0 .9.9 0 2 0h54a2 2 0 012 2v12a2 
2 0 01-2 2H2a2 2 0 01-2-2V2z" clip-rule="evenodd"></path><path fill="#fff" d="M6.3 9.3v3.2H5V4H8c1 0 1.7.2 2.3.7.6.5.8 1.2.8 2s-.2 1.5-.8 
2c-.5.4-1.3.6-2.3.6H6.3zm0-1.2h1.8c.6 0 1 0 1.2-.3.3-.3.5-.6.5-1.1 0-.5-.2-.8-.5-1.1-.2-.3-.6-.4-1.1-.4H6.3v3zm9.4-.6h-.6c-.6 0-1 
.2-1.3.7v4.3h-1.4V6.2h1.4v.7c.3-.6.8-.9 1.4-.9l.5.1v1.4zm3.6 5.1a3 3 0 01-2.2-.8c-.6-.6-.8-1.4-.8-2.3v-.2c0-.6 0-1.2.3-1.7s.6-.9 1-1.1c.5-.3 1-.5 
1.5-.5.9 0 1.6.3 2 .9.5.5.7 1.3.7 2.3v.6h-4.1c0 .5.2 1 .5 1.2.3.3.7.5 1.2.5a2 2 0 001.6-.8l.7.7c-.2.4-.6.7-1 1l-1.4.2zm-.2-5.4c-.4 0-.7.1-1 .4l-.4 
1.1h2.7c0-.5-.1-.9-.3-1.1-.3-.3-.6-.4-1-.4zm4.4 5.3V7.2h-1v-1h1v-.6c0-.7.1-1.3.5-1.6.4-.4 1-.6 1.7-.6h.8v1.2h-.6c-.7 0-1 .3-1 
1v.6h1.3v1h-1.3v5.3h-1.4zm6.4.1a3 3 0 01-2.2-.8c-.6-.6-.9-1.4-.9-2.3v-.2c0-.6.1-1.2.4-1.7.2-.5.6-.9 1-1.1.5-.3 1-.5 1.5-.5.9 0 1.5.3 2 .9.5.5.7 
1.3.7 2.3v.6h-4.1c0 .5.2 1 .5 1.2.3.3.7.5 1.1.5a2 2 0 001.6-.8l.8.7-1 1-1.4.2zm-.2-5.4c-.4 0-.7.1-1 .4-.2.3-.4.7-.4 
1.1H31c0-.5-.2-.9-.4-1.1-.2-.3-.5-.4-1-.4zm7.1.3h-.5c-.7 0-1.1.2-1.4.7v4.3h-1.4V6.2H35v.7c.3-.6.8-.9 1.4-.9l.5.1v1.4zm4.2 0h-.5c-.7 
0-1.1.2-1.3.7v4.3h-1.5V6.2h1.4v.7c.4-.6.8-.9 1.5-.9l.5.1v1.4zm3.6 5.1a3 3 0 01-2.2-.8c-.5-.6-.8-1.4-.8-2.3v-.2c0-.6.1-1.2.4-1.7.2-.5.5-.9 
1-1.1.4-.3 1-.5 1.5-.5.8 0 1.5.3 2 .9.4.5.7 1.3.7 2.3v.6H43c0 .5.2 1 .5 1.2.4.3.7.5 1.2.5a2 2 0 001.6-.8l.8.7-1 1-1.5.2zm-.1-5.4c-.4 0-.8.1-1 .4L43 
8.7h2.8c0-.5-.2-.9-.4-1.1-.2-.3-.6-.4-1-.4zm3.5 2c0-.9.2-1.7.7-2.3.4-.6 1-.9 1.8-.9a2 2 0 011.6.7V3.5h1.5v9h-1.3v-.7c-.5.6-1 .8-1.8.8-.7 
0-1.3-.3-1.8-.9a4 4 0 01-.7-2.4zm1.4.2c0 .7.2 1.2.4 1.5.3.4.6.6 1 .6.6 0 1-.3 1.3-.8V8c-.2-.5-.6-.8-1.2-.8-.5 0-.8.2-1 .6a3 3 0 00-.5 
1.6z"></path></svg></div><span style="margin-left: 10px;">Sonala.my</span></a><button class="Eg4UEE"><svg viewBox="0 0 16 16" 
class="shopee-svg-icon AxeMgG"><g fill-rule="evenodd"><path d="M15 4a1 1 0 01.993.883L16 5v9.932a.5.5 0 01-.82.385l-2.061-1.718-8.199.001a1 1 0 
01-.98-.8l-.016-.117-.108-1.284 8.058.001a2 2 0 001.976-1.692l.018-.155L14.293 4H15zm-2.48-4a1 1 0 011 1l-.003.077-.646 8.4a1 1 0 
01-.997.923l-8.994-.001-2.06 1.718a.5.5 0 01-.233.108l-.087.007a.5.5 0 01-.492-.41L0 11.732V1a1 1 0 011-1h11.52zM3.646 4.246a.5.5 0 000 
.708c.305.304.694.526 1.146.682A4.936 4.936 0 006.4 5.9c.464 0 1.02-.062 1.608-.264.452-.156.841-.378 1.146-.682a.5.5 0 
10-.708-.708c-.185.186-.445.335-.764.444a4.004 4.004 0 01-2.564 0c-.319-.11-.579-.258-.764-.444a.5.5 0 00-.708 0z"></path></g></svg></button><div 
class="cVlPY7"></div><div class="p1DEnN"><svg fill="none" viewBox="0 0 18 18" class="shopee-svg-icon KeOYUq icon-coin-line"><path stroke="#FFA600" 
stroke-width="1.3" d="M17.35 9A8.35 8.35 0 11.65 9a8.35 8.35 0 0116.7 0z"></path><path fill="#FFA600" fill-rule="evenodd" stroke="#FFA600" 
stroke-width=".2" d="M6.86 4.723c-.683.576-.998 1.627-.75 2.464.215.725.85 1.258 1.522 1.608.37.193.77.355 
1.177.463.1.027.2.051.3.08.098.03.196.062.294.096.06.021.121.044.182.067.017.006.107.041.04.014-.07-.028.071.03.087.037.286.124.56.27.82.44.114.076
.045.024.151.111a2.942 2.942 0 01.322.303c.087.093.046.042.114.146.18.275.245.478.235.8-.01.328-.14.659-.325.867-.47.53-1.232.73-1.934.696a4.727 
4.727 0 01-1.487-.307c-.45-.182-.852-.462-1.242-.737-.25-.176-.643-.04-.788.197-.17.279-.044.574.207.75.753.532 1.539.946 2.474 1.098.885.144 
1.731.124 2.563-.224.78-.326 1.416-.966 1.607-1.772.198-.838-.023-1.644-.61-2.29-.683-.753-1.722-1.17-2.706-1.43a4.563 4.563 0 
01-.543-.183c.122.048-.044-.02-.078-.035a4.77 4.77 0 01-.422-.212c-.594-.338-.955-.722-.872-1.369.105-.816.757-1.221 1.555-1.28.808-.06 1.648.135 
2.297.554.614.398 1.19-.553.58-.947-1.33-.86-3.504-1.074-4.77-.005z" clip-rule="evenodd"></path></svg>Shopee coins 
redeemable</div></div></div><section class="RqMReY" role="list"><div class="_9G37m"><div class="wsVAKH"><span class="lKqYHD">Bundle</span><span>Any 
2 enjoy RM1.00 off, up to RM5.00 off</span><span class="Vm8iNU"><a href="/bundle-deal/158531705967092?from=cart">Add more<svg viewBox="0 0 12 12" 
fill="none" width="12" height="12" color="#ee4d2d" class="MuMxsb"><path fill-rule="evenodd" clip-rule="evenodd" d="M9.293 6L4.146.854l.708-.708L10 
5.293a1 1 0 010 1.414l-5.146 5.147-.708-.707L9.293 6z" fill="currentColor"></path></svg></a></span></div><div class="lDiGJB kEMRam" 
role="listitem"><h4 class="a11y-hidden">cart_accessibility_item</h4><div class="f1bSN6"><div class="Xp4RLg"><label class="stardust-checkbox"><input 
class="stardust-checkbox__input" type="checkbox" aria-checked="false" aria-disabled="false" tabindex="0" role="checkbox" aria-label="Click here to 
select this product"><div class="stardust-checkbox__box"></div></label></div><div class="brf29Y"><div class="bzhajK"><a title="SONALA 1kg/2kg/4kg 
Dumbell Gym Dumbbell Exercise Fitness Exercise Home Weight Training Workout Neoprene Dumbell" 
href="/SONALA-1kg-2kg-4kg-Dumbell-Gym-Dumbbell-Exercise-Fitness-Exercise-Home-Weight-Training-Workout-Neoprene-Dumbell-i.1097454459.25951007347
?xptdk=015578b0-4f22-49df-bd06-d21f5450978b"><img class="jFEiVQ" src="https://down-my.img.susercontent.com/file/cn-11134207-7r98o-locb04xioahv96" 
alt="product image"></a><div class="Ou_0WX"><a class="c54pg1" title="SONALA 1kg/2kg/4kg Dumbell Gym Dumbbell Exercise Fitness Exercise Home Weight 
Training Workout Neoprene Dumbell" href="/SONALA-1kg-2kg-4kg-Dumbell-Gym-Dumbbell-Exercise-Fitness-Exercise-Home-Weight-Training-Workout-Neoprene
-Dumbell-i.1097454459.25951007347?xptdk=015578b0-4f22-49df-bd06-d21f5450978b">SONALA 1kg/2kg/4kg Dumbell Gym Dumbbell Exercise Fitness Exercise 
Home Weight Training Workout Neoprene Dumbell</a><img class="Kv1AvK" 
src="https://down-my.img.susercontent.com/file/my-50009109-07d26479b71d36d840c404c716d03602"><div class="gvFc9h"></div></div></div></div><div 
class="eHDC_o"><div class="qNRZqG"><button class="mM4TZ8" role="button" tabindex="0"><div class="iIg1CN">Variations:<div 
class="E33rwr"></div></div><div class="dDPSp3">Pink,1Pcs-3Kg</div></button><div></div></div></div><div class="gJyWia"><div><span class="vjkBXu 
tnTSPU">RM67.65</span><span class="vjkBXu">RM25.90</span></div></div><div class="sluy3i"><div class="GpmJtT shopee-input-quantity"><button 
class="WNSVcC" aria-label="Decrease"><svg enable-background="new 0 0 10 10" viewBox="0 0 10 10" x="0" y="0" class="shopee-svg-icon"><polygon 
points="4.5 4.5 3.5 4.5 0 4.5 0 5.5 3.5 5.5 4.5 5.5 10 5.5 10 4.5"></polygon></svg></button><input class="WNSVcC g2m9n4" type="text" 
role="spinbutton" aria-valuenow="1" value="1"><button class="WNSVcC" aria-label="Increase"><svg enable-background="new 0 0 10 10" viewBox="0 0 10 
10" x="0" y="0" class="shopee-svg-icon icon-plus-sign"><polygon points="10 4.5 5.5 4.5 5.5 0 4.5 0 4.5 4.5 0 4.5 0 5.5 4.5 5.5 4.5 10 5.5 10 5.5 
5.5 10 5.5"></polygon></svg></button></div></div><div class="HRvCAv"><span>RM25.90</span><span class="a11y-hidden">Total price: 
RM25.90</span></div><div class="bRSn43 TvSDdG"><button class="lSrQtj">Delete</button><div class="J8cCGR"><button class="shopee-button-no-outline 
slfWNx"><span class="wZrjgF">Find Similar</span><svg enable-background="new 0 0 15 15" viewBox="0 0 15 15" x="0" y="0" class="shopee-svg-icon 
f3N1Rf icon-down-arrow-filled"><path d="m6.5 12.9-6-7.9s-1.4-1.5.5-1.5h13s1.8 0 .6 1.5l-6 7.9c-.1 0-.9 1.3-2.1 
0z"></path></svg></button></div></div></div></div><div class="t89ViJ"></div></div></section><div class="ArX7yj"><svg fill="none" viewBox="0 -2 23 
22" class="shopee-svg-icon lGPe96 icon-voucher-line"><g filter="url(#voucher-filter0_d)"><mask id="a" fill="#fff"><path fill-rule="evenodd" 
clip-rule="evenodd" d="M1 2h18v2.32a1.5 1.5 0 000 2.75v.65a1.5 1.5 0 000 2.75v.65a1.5 1.5 0 000 2.75V16H1v-2.12a1.5 1.5 0 000-2.75v-.65a1.5 1.5 0 
000-2.75v-.65a1.5 1.5 0 000-2.75V2z"></path></mask><path d="M19 2h1V1h-1v1zM1 2V1H0v1h1zm18 2.32l.4.92.6-.26v-.66h-1zm0 
2.75h1v-.65l-.6-.26-.4.91zm0 .65l.4.92.6-.26v-.66h-1zm0 2.75h1v-.65l-.6-.26-.4.91zm0 .65l.4.92.6-.26v-.66h-1zm0 2.75h1v-.65l-.6-.26-.4.91zM19 
16v1h1v-1h-1zM1 16H0v1h1v-1zm0-2.12l-.4-.92-.6.26v.66h1zm0-2.75H0v.65l.6.26.4-.91zm0-.65l-.4-.92-.6.26v.66h1zm0-2.75H0v.65l.6.26.4-.91zm0-.65l-.4
-.92-.6.26v.66h1zm0-2.75H0v.65l.6.26.4-.91zM19 1H1v2h18V1zm1 3.32V2h-2v2.32h2zm-.9 1.38c0-.2.12-.38.3-.46l-.8-1.83a2.5 2.5 0 00-1.5 
2.29h2zm.3.46a.5.5 0 01-.3-.46h-2c0 1.03.62 1.9 1.5 2.3l.8-1.84zm.6 1.56v-.65h-2v.65h2zm-.9 1.38c0-.2.12-.38.3-.46l-.8-1.83a2.5 2.5 0 00-1.5 
2.29h2zm.3.46a.5.5 0 01-.3-.46h-2c0 1.03.62 1.9 1.5 2.3l.8-1.84zm.6 1.56v-.65h-2v.65h2zm-.9 1.38c0-.2.12-.38.3-.46l-.8-1.83a2.5 2.5 0 00-1.5 
2.29h2zm.3.46a.5.5 0 01-.3-.46h-2c0 1.03.62 1.9 1.5 2.3l.8-1.84zM20 16v-2.13h-2V16h2zM1 17h18v-2H1v2zm-1-3.12V16h2v-2.12H0zm1.4.91a2.5 2.5 0 
001.5-2.29h-2a.5.5 0 01-.3.46l.8 1.83zm1.5-2.29a2.5 2.5 0 00-1.5-2.3l-.8 1.84c.18.08.3.26.3.46h2zM0 10.48v.65h2v-.65H0zM.9 9.1a.5.5 0 01-.3.46l.8 
1.83A2.5 2.5 0 002.9 9.1h-2zm-.3-.46c.18.08.3.26.3.46h2a2.5 2.5 0 00-1.5-2.3L.6 8.65zM0 7.08v.65h2v-.65H0zM.9 5.7a.5.5 0 01-.3.46l.8 1.83A2.5 2.5 0 
002.9 5.7h-2zm-.3-.46c.18.08.3.26.3.46h2a2.5 2.5 0 00-1.5-2.3L.6 5.25zM0 2v2.33h2V2H0z" mask="url(#a)"></path></g><path clip-rule="evenodd" 
d="M6.49 14.18h.86v-1.6h-.86v1.6zM6.49 11.18h.86v-1.6h-.86v1.6zM6.49 8.18h.86v-1.6h-.86v1.6zM6.49 5.18h.86v-1.6h-.86v1.6z"></path><defs><filter 
id="voucher-filter0_d" x="0" y="1" width="20" height="16" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB"><feFlood 
flood-opacity="0" result="BackgroundImageFix"></feFlood><feColorMatrix in="SourceAlpha" values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 127 
0"></feColorMatrix><feOffset></feOffset><feGaussianBlur stdDeviation=".5"></feGaussianBlur><feColorMatrix values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
0 0.09 0"></feColorMatrix><feBlend in2="BackgroundImageFix" result="effect1_dropShadow"></feBlend><feBlend in="SourceGraphic" 
in2="effect1_dropShadow" result="shape"></feBlend></filter></defs></svg><div class="N9nCmB"><div class="nKTIzW">Up to RM15 off voucher 
available</div><div class="JC72Dv"><button class="qe2YoR">More Vouchers</button><div style="display: contents;"></div></div></div></div><div 
class="_RPX38"><img width="20" height="20" src="https://deo.shopeemobile.com/shopee/shopee-pcmall-live-sg/cart/094f639ce7dff28ced5b.png" 
alt="fs-icon"><div class="Cmb29y">Up to RM5.00 off shipping for orders over RM0.00</div><div class="shopee-drawer" id="pc-drawer-id-2" 
tabindex="0"><span class="Eb1Wor" aria-describedby="1097454459_shipping_discount"> Learn more </span></div></div></section><section 
class="AuhAvM"><h3 class="a11y-hidden">Shop Section</h3><div class="JsC6Oq"><div class="gzSvrb"><div class="Ll5dDW"><label 
class="stardust-checkbox"><input class="stardust-checkbox__input" type="checkbox" aria-checked="false" tabindex="0" role="checkbox" 
aria-label="Click here to select all products in WM GYM"><div class="stardust-checkbox__box"></div></label></div><a class="QcqMX5" 
href="/wmgym?categoryId=100637&amp;entryPoint=cart&amp;itemId=23384745341"><div class="Koi0Pw"><svg xmlns="http://www.w3.org/2000/svg" width="64" 
height="16" fill="none"><title>Preferred Seller Plus</title><path fill="#EE4D2D" fill-rule="evenodd" d="M0 2C0 .9.9 0 2 0h60a2 2 0 012 2v12a2 2 0 
01-2 2H2a2 2 0 01-2-2V2z" clip-rule="evenodd"></path><path fill="#fff" d="M6.3 9.3v3.2H5V4H8c1 0 1.7.2 2.3.7.6.5.8 1.2.8 2s-.2 1.5-.8 
2c-.5.4-1.3.6-2.3.6H6.3zm0-1.2h1.8c.6 0 1 0 1.2-.3.3-.3.5-.6.5-1.1 0-.5-.2-.8-.5-1.1-.2-.3-.6-.4-1.1-.4H6.3v3zm9.4-.6h-.6c-.6 0-1 
.2-1.3.7v4.3h-1.4V6.2h1.4v.7c.3-.6.8-.9 1.4-.9l.5.1v1.4zm3.6 5.1a3 3 0 01-2.2-.8c-.6-.6-.8-1.4-.8-2.3v-.2c0-.6 0-1.2.3-1.7s.6-.9 1-1.1c.5-.3 1-.5 
1.5-.5.9 0 1.6.3 2 .9.5.5.7 1.3.7 2.3v.6h-4.1c0 .5.2 1 .5 1.2.3.3.7.5 1.2.5a2 2 0 001.6-.8l.7.7c-.2.4-.6.7-1 1l-1.4.2zm-.2-5.4c-.4 0-.7.1-1 .4l-.4 
1.1h2.7c0-.5-.1-.9-.3-1.1-.3-.3-.6-.4-1-.4zm4.4 5.3V7.2h-1v-1h1v-.6c0-.7.1-1.3.5-1.6.4-.4 1-.6 1.7-.6h.8v1.2h-.6c-.7 0-1 .3-1 
1v.6h1.3v1h-1.3v5.3h-1.4zm6.4.1a3 3 0 01-2.2-.8c-.6-.6-.9-1.4-.9-2.3v-.2c0-.6.1-1.2.4-1.7.2-.5.6-.9 1-1.1.5-.3 1-.5 1.5-.5.9 0 1.5.3 2 .9.5.5.7 
1.3.7 2.3v.6h-4.1c0 .5.2 1 .5 1.2.3.3.7.5 1.1.5a2 2 0 001.6-.8l.8.7-1 1-1.4.2zm-.2-5.4c-.4 0-.7.1-1 .4-.2.3-.4.7-.4 
1.1H31c0-.5-.2-.9-.4-1.1-.2-.3-.5-.4-1-.4zm7.1.3h-.5c-.7 0-1.1.2-1.4.7v4.3h-1.4V6.2H35v.7c.3-.6.8-.9 1.4-.9l.5.1v1.4zm4.2 0h-.5c-.7 
0-1.1.2-1.3.7v4.3h-1.5V6.2h1.4v.7c.4-.6.8-.9 1.5-.9l.5.1v1.4zm3.6 5.1a3 3 0 01-2.2-.8c-.5-.6-.8-1.4-.8-2.3v-.2c0-.6.1-1.2.4-1.7.2-.5.5-.9 
1-1.1.4-.3 1-.5 1.5-.5.8 0 1.5.3 2 .9.4.5.7 1.3.7 2.3v.6H43c0 .5.2 1 .5 1.2.4.3.7.5 1.2.5a2 2 0 001.6-.8l.8.7-1 1-1.5.2zm-.1-5.4c-.4 0-.8.1-1 .4L43 
8.7h2.8c0-.5-.2-.9-.4-1.1-.2-.3-.6-.4-1-.4zm3.5 2c0-.9.2-1.7.7-2.3.4-.6 1-.9 1.8-.9a2 2 0 011.6.7V3.5h1.5v9h-1.3v-.7c-.5.6-1 .8-1.8.8-.7 
0-1.3-.3-1.8-.9a4 4 0 01-.7-2.4zm1.4.2c0 .7.2 1.2.4 1.5.3.4.6.6 1 .6.6 0 1-.3 1.3-.8V8c-.2-.5-.6-.8-1.2-.8-.5 0-.8.2-1 .6a3 3 0 00-.5 
1.6z"></path><g clip-path="url(#clip0)"><path fill="#fff" d="M58 8.2h2.2v1.6H58V12h-1.6V9.8h-2.2V8.2h2.2V6H58v2.3z"></path></g><defs><clipPath 
id="clip0"><path fill="#fff" d="M0 0h7v16H0z" transform="translate(54)"></path></clipPath></defs></svg></div><span style="margin-left: 10px;">WM 
GYM</span></a><button class="Eg4UEE"><svg viewBox="0 0 16 16" class="shopee-svg-icon AxeMgG"><g fill-rule="evenodd"><path d="M15 4a1 1 0 
01.993.883L16 5v9.932a.5.5 0 01-.82.385l-2.061-1.718-8.199.001a1 1 0 01-.98-.8l-.016-.117-.108-1.284 8.058.001a2 2 0 001.976-1.692l.018-.155L14.293 
4H15zm-2.48-4a1 1 0 011 1l-.003.077-.646 8.4a1 1 0 01-.997.923l-8.994-.001-2.06 1.718a.5.5 0 01-.233.108l-.087.007a.5.5 0 01-.492-.41L0 11.732V1a1 
1 0 011-1h11.52zM3.646 4.246a.5.5 0 000 .708c.305.304.694.526 1.146.682A4.936 4.936 0 006.4 5.9c.464 0 1.02-.062 1.608-.264.452-.156.841-.378 
1.146-.682a.5.5 0 10-.708-.708c-.185.186-.445.335-.764.444a4.004 4.004 0 01-2.564 0c-.319-.11-.579-.258-.764-.444a.5.5 0 00-.708 
0z"></path></g></svg></button><div class="cVlPY7"></div><div class="p1DEnN"><svg fill="none" viewBox="0 0 18 18" class="shopee-svg-icon KeOYUq 
icon-coin-line"><path stroke="#FFA600" stroke-width="1.3" d="M17.35 9A8.35 8.35 0 11.65 9a8.35 8.35 0 0116.7 0z"></path><path fill="#FFA600" 
fill-rule="evenodd" stroke="#FFA600" stroke-width=".2" d="M6.86 4.723c-.683.576-.998 1.627-.75 2.464.215.725.85 1.258 1.522 1.608.37.193.77.355 
1.177.463.1.027.2.051.3.08.098.03.196.062.294.096.06.021.121.044.182.067.017.006.107.041.04.014-.07-.028.071.03.087.037.286.124.56.27.82.44.114.076
.045.024.151.111a2.942 2.942 0 01.322.303c.087.093.046.042.114.146.18.275.245.478.235.8-.01.328-.14.659-.325.867-.47.53-1.232.73-1.934.696a4.727 
4.727 0 01-1.487-.307c-.45-.182-.852-.462-1.242-.737-.25-.176-.643-.04-.788.197-.17.279-.044.574.207.75.753.532 1.539.946 2.474 1.098.885.144 
1.731.124 2.563-.224.78-.326 1.416-.966 1.607-1.772.198-.838-.023-1.644-.61-2.29-.683-.753-1.722-1.17-2.706-1.43a4.563 4.563 0 
01-.543-.183c.122.048-.044-.02-.078-.035a4.77 4.77 0 01-.422-.212c-.594-.338-.955-.722-.872-1.369.105-.816.757-1.221 1.555-1.28.808-.06 1.648.135 
2.297.554.614.398 1.19-.553.58-.947-1.33-.86-3.504-1.074-4.77-.005z" clip-rule="evenodd"></path></svg>Shopee coins 
redeemable</div></div></div><section class="RqMReY" role="list"><div class="lDiGJB" role="listitem"><h4 
class="a11y-hidden">cart_accessibility_item</h4><div class="f1bSN6"><div class="Xp4RLg"><label class="stardust-checkbox"><input 
class="stardust-checkbox__input" type="checkbox" aria-checked="false" aria-disabled="false" tabindex="0" role="checkbox" aria-label="Click here to 
select this product"><div class="stardust-checkbox__box"></div></label></div><div class="brf29Y"><div class="bzhajK"><a title="[5KGx2] 10kg Set 
Hexagon Premium Dumbbell Dumbells Sport Gym Fitness Exercise Weight Training Equipment 哑铃 健身" 
href="/-5KGx2-10kg-Set-Hexagon-Premium-Dumbbell-Dumbells-Sport-Gym-Fitness-Exercise-Weight-Training-Equipment-哑铃-健身-i.811486108.23384745341?xptdk
=c8e42bfb-f0a0-4d32-abdc-dcf8fbe8d15e"><img class="jFEiVQ" src="https://down-my.img.susercontent.com/file/my-11134207-7r98x-lnbhnlt4du4c18" 
alt="product image"></a><div class="Ou_0WX"><a class="c54pg1" title="[5KGx2] 10kg Set Hexagon Premium Dumbbell Dumbells Sport Gym Fitness Exercise 
Weight Training Equipment 哑铃 健身" href="/-5KGx2-10kg-Set-Hexagon-Premium-Dumbbell-Dumbells-Sport-Gym-Fitness-Exercise-Weight-Training-Equipment
-哑铃-健身-i.811486108.23384745341?xptdk=c8e42bfb-f0a0-4d32-abdc-dcf8fbe8d15e">[5KGx2] 10kg Set Hexagon Premium Dumbbell Dumbells Sport Gym Fitness 
Exercise Weight Training Equipment 哑铃 健身</a><img class="Kv1AvK" 
src="https://down-my.img.susercontent.com/file/my-50009109-07d26479b71d36d840c404c716d03602"><div class="gvFc9h"></div></div></div></div><div 
class="eHDC_o"><div class="qNRZqG"><button class="mM4TZ8" role="button" tabindex="0"><div class="iIg1CN">Variations:<div 
class="E33rwr"></div></div><div class="dDPSp3">5Kg x 2 Pcs [10Kg]</div></button><div></div></div></div><div class="gJyWia"><div><span class="vjkBXu 
tnTSPU">RM49.00</span><span class="vjkBXu">RM36.99</span></div></div><div class="sluy3i"><div class="GpmJtT shopee-input-quantity"><button 
class="WNSVcC" aria-label="Decrease"><svg enable-background="new 0 0 10 10" viewBox="0 0 10 10" x="0" y="0" class="shopee-svg-icon"><polygon 
points="4.5 4.5 3.5 4.5 0 4.5 0 5.5 3.5 5.5 4.5 5.5 10 5.5 10 4.5"></polygon></svg></button><input class="WNSVcC g2m9n4" type="text" 
role="spinbutton" aria-valuenow="1" value="1"><button class="WNSVcC" aria-label="Increase"><svg enable-background="new 0 0 10 10" viewBox="0 0 10 
10" x="0" y="0" class="shopee-svg-icon icon-plus-sign"><polygon points="10 4.5 5.5 4.5 5.5 0 4.5 0 4.5 4.5 0 4.5 0 5.5 4.5 5.5 4.5 10 5.5 10 5.5 
5.5 10 5.5"></polygon></svg></button></div></div><div class="HRvCAv"><span>RM36.99</span><span class="a11y-hidden">Total price: 
RM36.99</span></div><div class="bRSn43 TvSDdG"><button class="lSrQtj">Delete</button><div class="J8cCGR"><button class="shopee-button-no-outline 
slfWNx"><span class="wZrjgF">Find Similar</span><svg enable-background="new 0 0 15 15" viewBox="0 0 15 15" x="0" y="0" class="shopee-svg-icon 
f3N1Rf icon-down-arrow-filled"><path d="m6.5 12.9-6-7.9s-1.4-1.5.5-1.5h13s1.8 0 .6 1.5l-6 7.9c-.1 0-.9 1.3-2.1 
0z"></path></svg></button></div></div></div></div></section><div class="_RPX38"><img width="20" height="20" 
src="https://deo.shopeemobile.com/shopee/shopee-pcmall-live-sg/cart/094f639ce7dff28ced5b.png" alt="fs-icon"><div class="Cmb29y">Up to RM5.00 off 
shipping for orders over RM0.00</div><div class="shopee-drawer" id="pc-drawer-id-3" tabindex="0"><span class="Eb1Wor" 
aria-describedby="811486108_shipping_discount"> Learn more </span></div></div></section><section class="AuhAvM"><h3 class="a11y-hidden">Shop 
Section</h3><div class="JsC6Oq"><div class="gzSvrb"><div class="Ll5dDW"><label class="stardust-checkbox"><input class="stardust-checkbox__input" 
type="checkbox" aria-checked="false" tabindex="0" role="checkbox" aria-label="Click here to select all products in fuyogi1.my"><div 
class="stardust-checkbox__box"></div></label></div><a class="QcqMX5" 
href="/fuyogi1.my?categoryId=100637&amp;entryPoint=cart&amp;itemId=20739313537"><div class="Koi0Pw"><svg xmlns="http://www.w3.org/2000/svg" 
width="58" height="16" fill="none"><title>Preferred Seller</title><path fill="#EE4D2D" fill-rule="evenodd" d="M0 2C0 .9.9 0 2 0h54a2 2 0 012 2v12a2 
2 0 01-2 2H2a2 2 0 01-2-2V2z" clip-rule="evenodd"></path><path fill="#fff" d="M6.3 9.3v3.2H5V4H8c1 0 1.7.2 2.3.7.6.5.8 1.2.8 2s-.2 1.5-.8 
2c-.5.4-1.3.6-2.3.6H6.3zm0-1.2h1.8c.6 0 1 0 1.2-.3.3-.3.5-.6.5-1.1 0-.5-.2-.8-.5-1.1-.2-.3-.6-.4-1.1-.4H6.3v3zm9.4-.6h-.6c-.6 0-1 
.2-1.3.7v4.3h-1.4V6.2h1.4v.7c.3-.6.8-.9 1.4-.9l.5.1v1.4zm3.6 5.1a3 3 0 01-2.2-.8c-.6-.6-.8-1.4-.8-2.3v-.2c0-.6 0-1.2.3-1.7s.6-.9 1-1.1c.5-.3 1-.5 
1.5-.5.9 0 1.6.3 2 .9.5.5.7 1.3.7 2.3v.6h-4.1c0 .5.2 1 .5 1.2.3.3.7.5 1.2.5a2 2 0 001.6-.8l.7.7c-.2.4-.6.7-1 1l-1.4.2zm-.2-5.4c-.4 0-.7.1-1 .4l-.4 
1.1h2.7c0-.5-.1-.9-.3-1.1-.3-.3-.6-.4-1-.4zm4.4 5.3V7.2h-1v-1h1v-.6c0-.7.1-1.3.5-1.6.4-.4 1-.6 1.7-.6h.8v1.2h-.6c-.7 0-1 .3-1 
1v.6h1.3v1h-1.3v5.3h-1.4zm6.4.1a3 3 0 01-2.2-.8c-.6-.6-.9-1.4-.9-2.3v-.2c0-.6.1-1.2.4-1.7.2-.5.6-.9 1-1.1.5-.3 1-.5 1.5-.5.9 0 1.5.3 2 .9.5.5.7 
1.3.7 2.3v.6h-4.1c0 .5.2 1 .5 1.2.3.3.7.5 1.1.5a2 2 0 001.6-.8l.8.7-1 1-1.4.2zm-.2-5.4c-.4 0-.7.1-1 .4-.2.3-.4.7-.4 
1.1H31c0-.5-.2-.9-.4-1.1-.2-.3-.5-.4-1-.4zm7.1.3h-.5c-.7 0-1.1.2-1.4.7v4.3h-1.4V6.2H35v.7c.3-.6.8-.9 1.4-.9l.5.1v1.4zm4.2 0h-.5c-.7 
0-1.1.2-1.3.7v4.3h-1.5V6.2h1.4v.7c.4-.6.8-.9 1.5-.9l.5.1v1.4zm3.6 5.1a3 3 0 01-2.2-.8c-.5-.6-.8-1.4-.8-2.3v-.2c0-.6.1-1.2.4-1.7.2-.5.5-.9 
1-1.1.4-.3 1-.5 1.5-.5.8 0 1.5.3 2 .9.4.5.7 1.3.7 2.3v.6H43c0 .5.2 1 .5 1.2.4.3.7.5 1.2.5a2 2 0 001.6-.8l.8.7-1 1-1.5.2zm-.1-5.4c-.4 0-.8.1-1 .4L43 
8.7h2.8c0-.5-.2-.9-.4-1.1-.2-.3-.6-.4-1-.4zm3.5 2c0-.9.2-1.7.7-2.3.4-.6 1-.9 1.8-.9a2 2 0 011.6.7V3.5h1.5v9h-1.3v-.7c-.5.6-1 .8-1.8.8-.7 
0-1.3-.3-1.8-.9a4 4 0 01-.7-2.4zm1.4.2c0 .7.2 1.2.4 1.5.3.4.6.6 1 .6.6 0 1-.3 1.3-.8V8c-.2-.5-.6-.8-1.2-.8-.5 0-.8.2-1 .6a3 3 0 00-.5 
1.6z"></path></svg></div><span style="margin-left: 10px;">fuyogi1.my</span></a><button class="Eg4UEE"><svg viewBox="0 0 16 16" 
class="shopee-svg-icon AxeMgG"><g fill-rule="evenodd"><path d="M15 4a1 1 0 01.993.883L16 5v9.932a.5.5 0 01-.82.385l-2.061-1.718-8.199.001a1 1 0 
01-.98-.8l-.016-.117-.108-1.284 8.058.001a2 2 0 001.976-1.692l.018-.155L14.293 4H15zm-2.48-4a1 1 0 011 1l-.003.077-.646 8.4a1 1 0 
01-.997.923l-8.994-.001-2.06 1.718a.5.5 0 01-.233.108l-.087.007a.5.5 0 01-.492-.41L0 11.732V1a1 1 0 011-1h11.52zM3.646 4.246a.5.5 0 000 
.708c.305.304.694.526 1.146.682A4.936 4.936 0 006.4 5.9c.464 0 1.02-.062 1.608-.264.452-.156.841-.378 1.146-.682a.5.5 0 
10-.708-.708c-.185.186-.445.335-.764.444a4.004 4.004 0 01-2.564 0c-.319-.11-.579-.258-.764-.444a.5.5 0 00-.708 0z"></path></g></svg></button><div 
class="cVlPY7"></div><div class="p1DEnN"><svg fill="none" viewBox="0 0 18 18" class="shopee-svg-icon KeOYUq icon-coin-line"><path stroke="#FFA600" 
stroke-width="1.3" d="M17.35 9A8.35 8.35 0 11.65 9a8.35 8.35 0 0116.7 0z"></path><path fill="#FFA600" fill-rule="evenodd" stroke="#FFA600" 
stroke-width=".2" d="M6.86 4.723c-.683.576-.998 1.627-.75 2.464.215.725.85 1.258 1.522 1.608.37.193.77.355 
1.177.463.1.027.2.051.3.08.098.03.196.062.294.096.06.021.121.044.182.067.017.006.107.041.04.014-.07-.028.071.03.087.037.286.124.56.27.82.44.114.076
.045.024.151.111a2.942 2.942 0 01.322.303c.087.093.046.042.114.146.18.275.245.478.235.8-.01.328-.14.659-.325.867-.47.53-1.232.73-1.934.696a4.727 
4.727 0 01-1.487-.307c-.45-.182-.852-.462-1.242-.737-.25-.176-.643-.04-.788.197-.17.279-.044.574.207.75.753.532 1.539.946 2.474 1.098.885.144 
1.731.124 2.563-.224.78-.326 1.416-.966 1.607-1.772.198-.838-.023-1.644-.61-2.29-.683-.753-1.722-1.17-2.706-1.43a4.563 4.563 0 
01-.543-.183c.122.048-.044-.02-.078-.035a4.77 4.77 0 01-.422-.212c-.594-.338-.955-.722-.872-1.369.105-.816.757-1.221 1.555-1.28.808-.06 1.648.135 
2.297.554.614.398 1.19-.553.58-.947-1.33-.86-3.504-1.074-4.77-.005z" clip-rule="evenodd"></path></svg>Shopee coins 
redeemable</div></div></div><section class="RqMReY" role="list"><div class="lDiGJB" role="listitem"><h4 
class="a11y-hidden">cart_accessibility_item</h4><div class="f1bSN6"><div class="Xp4RLg"><label class="stardust-checkbox"><input 
class="stardust-checkbox__input" type="checkbox" aria-checked="false" aria-disabled="false" tabindex="0" role="checkbox" aria-label="Click here to 
select this product"><div class="stardust-checkbox__box"></div></label></div><div class="brf29Y"><div class="bzhajK"><a title="FUYOGI Dumbbell Set 
1KG*2 Neoprene Workout Exercise Home Weight Training 2KG" 
href="/FUYOGI-Dumbbell-Set-1KG*2-Neoprene-Workout-Exercise-Home-Weight-Training-2KG-i.848739804.20739313537?xptdk=7e7e3f57-234b-43b8-a1b9
-221e21b28091"><img class="jFEiVQ" src="https://down-my.img.susercontent.com/file/cn-11134207-7r98o-lmr9ol8tiqjoe4" alt="product image"></a><div 
class="Ou_0WX"><a class="c54pg1" title="FUYOGI Dumbbell Set 1KG*2 Neoprene Workout Exercise Home Weight Training 2KG" 
href="/FUYOGI-Dumbbell-Set-1KG*2-Neoprene-Workout-Exercise-Home-Weight-Training-2KG-i.848739804.20739313537?xptdk=7e7e3f57-234b-43b8-a1b9
-221e21b28091">FUYOGI Dumbbell Set 1KG*2 Neoprene Workout Exercise Home Weight Training 2KG</a><img class="Kv1AvK" 
src="https://down-my.img.susercontent.com/file/my-50009109-07d26479b71d36d840c404c716d03602"><div class="gvFc9h"></div></div></div><div 
class="kG42T8 bzhajK"><svg height="21" viewBox="0 0 171 21" width="171" class="shopee-svg-icon icon-flash-sale QUePGT"><path d="m686.074219 
522.083984h2.851562c.136719 1.142578 1.289063 1.875 2.949219 1.875 1.533203 0 2.617188-.742187 2.617188-1.80664 
0-.898438-.703126-1.416016-2.431641-1.78711l-1.835938-.390625c-2.568359-.537109-3.828125-1.875-3.828125-4.023437 0-2.65625 2.138672-4.404297 
5.390625-4.404297 3.105469 0 5.302735 1.738281 5.390625 4.248047h-2.773437c-.136719-1.113281-1.171875-1.855469-2.597656-1.855469-1.47461 
0-2.451172.683594-2.451172 1.757813 0 .86914.673828 1.367187 2.324219 1.71875l1.699218.361328c2.832032.595703 4.052735 1.816406 4.052735 4.003906 0 
2.841797-2.177735 4.580078-5.712891 4.580078-3.359375 0-5.537109-1.65039-5.644531-4.277344zm26.608941 
3.916016h-2.949219v-5.888672h-6.347656v5.888672h-2.949219v-14.091797h2.949219v5.683594h6.347656v-5.683594h2.949219zm9.8023-14.453125c4.160156 0 
6.767578 2.841797 6.767578 7.402344 0 4.570312-2.597656 7.412109-6.767578 7.412109-4.179687 0-6.787109-2.841797-6.787109-7.412109 0-4.570313 
2.646484-7.402344 6.787109-7.402344zm0 2.587891c-2.285156 0-3.769531 1.865234-3.769531 4.814453 0 2.939453 1.455078 4.824219 3.769531 4.824219 
2.294922 0 3.759766-1.884766 3.759766-4.824219 0-2.949219-1.464844-4.814453-3.759766-4.814453zm15.769097 12.226562c-4.082031 
0-6.611328-2.822266-6.611328-7.412109 0-4.580078 2.519531-7.402344 6.611328-7.402344 3.339844 0 5.898438 2.216797 6.113282 
5.283203h-2.871094c-.283203-1.621094-1.5625-2.685547-3.242188-2.685547-2.216797 0-3.59375 1.835938-3.59375 4.804688s1.376953 4.814453 3.603516 
4.814453c1.689453 0 2.958984-.996094 3.242187-2.548828h2.871094c-.24414 3.046875-2.724609 5.146484-6.123047 
5.146484zm12.009332-.361328h-2.949219v-14.091797h2.949219v6.279297h.175781l5.205078-6.279297h3.28125l-5.136718 6.181641 5.498046 
7.910156h-3.535156l-4.091797-5.898438-1.396484 1.650391zm14.411675 0h-2.949219v-14.091797h2.949219zm6.462457 
0h-2.822266v-14.091797h2.460938l6.484375 8.779297h.175781v-8.779297h2.822266v14.091797h-2.441407l-6.503906-8.818359h-.175781zm25.144097-5.751953c0 
3.769531-2.402344 6.113281-6.25 6.113281-4.189453 0-6.757812-2.8125-6.757812-7.421875 0-4.541015 2.58789-7.392578 6.689453-7.392578 3.330078 0 
5.78125 1.923828 6.191406 4.853516h-2.929688c-.439453-1.425782-1.621093-2.25586-3.261718-2.25586-2.275391 0-3.671875 1.806641-3.671875 4.765625 0 
3.017578 1.464843 4.853516 3.789062 4.853516 1.933594 0 3.271485-1.142578 3.330078-2.841797l.009766-.253906h-3.056641v-2.216797h5.917969zm7.788195 
1.835937h2.851562c.136719 1.142578 1.289063 1.875 2.949219 1.875 1.533203 0 2.617187-.742187 2.617187-1.80664 
0-.898438-.703125-1.416016-2.43164-1.78711l-1.835938-.390625c-2.568359-.537109-3.828125-1.875-3.828125-4.023437 0-2.65625 2.138672-4.404297 
5.390625-4.404297 3.105469 0 5.302735 1.738281 5.390625 4.248047h-2.773437c-.136719-1.113281-1.171875-1.855469-2.597657-1.855469-1.474609 
0-2.451171.683594-2.451171 1.757813 0 .86914.673828 1.367187 2.324218 1.71875l1.699219.361328c2.832031.595703 4.052734 1.816406 4.052734 4.003906 0 
2.841797-2.177734 4.580078-5.71289 4.580078-3.359375 0-5.53711-1.65039-5.644531-4.277344zm23.415581 3.916016-1.064453-3.359375h-4.951172l-1.083984 
3.359375h-2.958985l4.892578-14.091797h3.466797l4.892578 14.091797zm-3.613281-11.162109-1.767578 5.527343h3.691406l-1.748047-5.527343zm18.649956 
8.59375v2.568359h-9.21875v-14.091797h2.949219v11.523438zm12.233941.048828v2.519531h-9.335937v-14.091797h9.335937v2.519531h-6.386718v3.291016h6
.02539v2.333984h-6.02539v3.427735z" fill="currentColor" fill-rule="evenodd" transform="translate(-685 -509)"></path></svg>Ends at 09:00:00 23 
Feb</div></div><div class="eHDC_o"><div class="qNRZqG"><button class="mM4TZ8" role="button" tabindex="0"><div class="iIg1CN">Variations:<div 
class="E33rwr"></div></div><div class="dDPSp3">Cherry Pink,2Pcs 1.5KG</div></button><div></div></div></div><div class="gJyWia"><div><span 
class="vjkBXu tnTSPU">RM49.00</span><span class="vjkBXu">RM26.90</span></div></div><div class="sluy3i"><div class="GpmJtT 
shopee-input-quantity"><button class="WNSVcC" aria-label="Decrease"><svg enable-background="new 0 0 10 10" viewBox="0 0 10 10" x="0" y="0" 
class="shopee-svg-icon"><polygon points="4.5 4.5 3.5 4.5 0 4.5 0 5.5 3.5 5.5 4.5 5.5 10 5.5 10 4.5"></polygon></svg></button><input class="WNSVcC 
g2m9n4" type="text" role="spinbutton" aria-valuenow="1" value="1"><button class="WNSVcC" aria-label="Increase"><svg enable-background="new 0 0 10 
10" viewBox="0 0 10 10" x="0" y="0" class="shopee-svg-icon icon-plus-sign"><polygon points="10 4.5 5.5 4.5 5.5 0 4.5 0 4.5 4.5 0 4.5 0 5.5 4.5 5.5 
4.5 10 5.5 10 5.5 5.5 10 5.5"></polygon></svg></button></div><div class="PwuHYD">8 items left</div></div><div 
class="HRvCAv"><span>RM26.90</span><span class="a11y-hidden">Total price: RM26.90</span></div><div class="bRSn43 TvSDdG"><button 
class="lSrQtj">Delete</button><div class="J8cCGR"><button class="shopee-button-no-outline slfWNx"><span class="wZrjgF">Find Similar</span><svg 
enable-background="new 0 0 15 15" viewBox="0 0 15 15" x="0" y="0" class="shopee-svg-icon f3N1Rf icon-down-arrow-filled"><path d="m6.5 
12.9-6-7.9s-1.4-1.5.5-1.5h13s1.8 0 .6 1.5l-6 7.9c-.1 0-.9 1.3-2.1 0z"></path></svg></button></div></div></div></div><div class="RIfxP9"></div><div 
class="lDiGJB" role="listitem"><h4 class="a11y-hidden">cart_accessibility_item</h4><div class="f1bSN6"><div class="Xp4RLg"><label 
class="stardust-checkbox"><input class="stardust-checkbox__input" type="checkbox" aria-checked="false" aria-disabled="false" tabindex="0" 
role="checkbox" aria-label="Click here to select this product"><div class="stardust-checkbox__box"></div></label></div><div class="brf29Y"><div 
class="bzhajK"><a title="FUYOGI Dumbbell Set 1KG*2 Neoprene Workout Exercise Home Weight Training 2KG" 
href="/FUYOGI-Dumbbell-Set-1KG*2-Neoprene-Workout-Exercise-Home-Weight-Training-2KG-i.848739804.20739313537?xptdk=17107b79-a037-42f2-81bc
-e2fe369f2906"><img class="jFEiVQ" src="https://down-my.img.susercontent.com/file/dd02879717eed6229b93456641773cd4" alt="product image"></a><div 
class="Ou_0WX"><a class="c54pg1" title="FUYOGI Dumbbell Set 1KG*2 Neoprene Workout Exercise Home Weight Training 2KG" 
href="/FUYOGI-Dumbbell-Set-1KG*2-Neoprene-Workout-Exercise-Home-Weight-Training-2KG-i.848739804.20739313537?xptdk=17107b79-a037-42f2-81bc
-e2fe369f2906">FUYOGI Dumbbell Set 1KG*2 Neoprene Workout Exercise Home Weight Training 2KG</a><img class="Kv1AvK" 
src="https://down-my.img.susercontent.com/file/my-50009109-07d26479b71d36d840c404c716d03602"><div class="gvFc9h"></div></div></div><div 
class="kG42T8 bzhajK"><svg height="21" viewBox="0 0 171 21" width="171" class="shopee-svg-icon icon-flash-sale QUePGT"><path d="m686.074219 
522.083984h2.851562c.136719 1.142578 1.289063 1.875 2.949219 1.875 1.533203 0 2.617188-.742187 2.617188-1.80664 
0-.898438-.703126-1.416016-2.431641-1.78711l-1.835938-.390625c-2.568359-.537109-3.828125-1.875-3.828125-4.023437 0-2.65625 2.138672-4.404297 
5.390625-4.404297 3.105469 0 5.302735 1.738281 5.390625 4.248047h-2.773437c-.136719-1.113281-1.171875-1.855469-2.597656-1.855469-1.47461 
0-2.451172.683594-2.451172 1.757813 0 .86914.673828 1.367187 2.324219 1.71875l1.699218.361328c2.832032.595703 4.052735 1.816406 4.052735 4.003906 0 
2.841797-2.177735 4.580078-5.712891 4.580078-3.359375 0-5.537109-1.65039-5.644531-4.277344zm26.608941 
3.916016h-2.949219v-5.888672h-6.347656v5.888672h-2.949219v-14.091797h2.949219v5.683594h6.347656v-5.683594h2.949219zm9.8023-14.453125c4.160156 0 
6.767578 2.841797 6.767578 7.402344 0 4.570312-2.597656 7.412109-6.767578 7.412109-4.179687 0-6.787109-2.841797-6.787109-7.412109 0-4.570313 
2.646484-7.402344 6.787109-7.402344zm0 2.587891c-2.285156 0-3.769531 1.865234-3.769531 4.814453 0 2.939453 1.455078 4.824219 3.769531 4.824219 
2.294922 0 3.759766-1.884766 3.759766-4.824219 0-2.949219-1.464844-4.814453-3.759766-4.814453zm15.769097 12.226562c-4.082031 
0-6.611328-2.822266-6.611328-7.412109 0-4.580078 2.519531-7.402344 6.611328-7.402344 3.339844 0 5.898438 2.216797 6.113282 
5.283203h-2.871094c-.283203-1.621094-1.5625-2.685547-3.242188-2.685547-2.216797 0-3.59375 1.835938-3.59375 4.804688s1.376953 4.814453 3.603516 
4.814453c1.689453 0 2.958984-.996094 3.242187-2.548828h2.871094c-.24414 3.046875-2.724609 5.146484-6.123047 
5.146484zm12.009332-.361328h-2.949219v-14.091797h2.949219v6.279297h.175781l5.205078-6.279297h3.28125l-5.136718 6.181641 5.498046 
7.910156h-3.535156l-4.091797-5.898438-1.396484 1.650391zm14.411675 0h-2.949219v-14.091797h2.949219zm6.462457 
0h-2.822266v-14.091797h2.460938l6.484375 8.779297h.175781v-8.779297h2.822266v14.091797h-2.441407l-6.503906-8.818359h-.175781zm25.144097-5.751953c0 
3.769531-2.402344 6.113281-6.25 6.113281-4.189453 0-6.757812-2.8125-6.757812-7.421875 0-4.541015 2.58789-7.392578 6.689453-7.392578 3.330078 0 
5.78125 1.923828 6.191406 4.853516h-2.929688c-.439453-1.425782-1.621093-2.25586-3.261718-2.25586-2.275391 0-3.671875 1.806641-3.671875 4.765625 0 
3.017578 1.464843 4.853516 3.789062 4.853516 1.933594 0 3.271485-1.142578 3.330078-2.841797l.009766-.253906h-3.056641v-2.216797h5.917969zm7.788195 
1.835937h2.851562c.136719 1.142578 1.289063 1.875 2.949219 1.875 1.533203 0 2.617187-.742187 2.617187-1.80664 
0-.898438-.703125-1.416016-2.43164-1.78711l-1.835938-.390625c-2.568359-.537109-3.828125-1.875-3.828125-4.023437 0-2.65625 2.138672-4.404297 
5.390625-4.404297 3.105469 0 5.302735 1.738281 5.390625 4.248047h-2.773437c-.136719-1.113281-1.171875-1.855469-2.597657-1.855469-1.474609 
0-2.451171.683594-2.451171 1.757813 0 .86914.673828 1.367187 2.324218 1.71875l1.699219.361328c2.832031.595703 4.052734 1.816406 4.052734 4.003906 0 
2.841797-2.177734 4.580078-5.71289 4.580078-3.359375 0-5.53711-1.65039-5.644531-4.277344zm23.415581 3.916016-1.064453-3.359375h-4.951172l-1.083984 
3.359375h-2.958985l4.892578-14.091797h3.466797l4.892578 14.091797zm-3.613281-11.162109-1.767578 5.527343h3.691406l-1.748047-5.527343zm18.649956 
8.59375v2.568359h-9.21875v-14.091797h2.949219v11.523438zm12.233941.048828v2.519531h-9.335937v-14.091797h9.335937v2.519531h-6.386718v3.291016h6
.02539v2.333984h-6.02539v3.427735z" fill="currentColor" fill-rule="evenodd" transform="translate(-685 -509)"></path></svg>Ends at 09:00:00 23 
Feb</div></div><div class="eHDC_o"><div class="qNRZqG"><button class="mM4TZ8" role="button" tabindex="0"><div class="iIg1CN">Variations:<div 
class="E33rwr"></div></div><div class="dDPSp3">Blue,2Pcs 1.5KG</div></button><div></div></div></div><div class="gJyWia"><div><span class="vjkBXu 
tnTSPU">RM49.00</span><span class="vjkBXu">RM26.90</span></div></div><div class="sluy3i"><div class="GpmJtT shopee-input-quantity"><button 
class="WNSVcC" aria-label="Decrease"><svg enable-background="new 0 0 10 10" viewBox="0 0 10 10" x="0" y="0" class="shopee-svg-icon"><polygon 
points="4.5 4.5 3.5 4.5 0 4.5 0 5.5 3.5 5.5 4.5 5.5 10 5.5 10 4.5"></polygon></svg></button><input class="WNSVcC g2m9n4" type="text" 
role="spinbutton" aria-valuenow="1" value="1"><button class="WNSVcC" aria-label="Increase"><svg enable-background="new 0 0 10 10" viewBox="0 0 10 
10" x="0" y="0" class="shopee-svg-icon icon-plus-sign"><polygon points="10 4.5 5.5 4.5 5.5 0 4.5 0 4.5 4.5 0 4.5 0 5.5 4.5 5.5 4.5 10 5.5 10 5.5 
5.5 10 5.5"></polygon></svg></button></div></div><div class="HRvCAv"><span>RM26.90</span><span class="a11y-hidden">Total price: 
RM26.90</span></div><div class="bRSn43 TvSDdG"><button class="lSrQtj">Delete</button><div class="J8cCGR"><button class="shopee-button-no-outline 
slfWNx"><span class="wZrjgF">Find Similar</span><svg enable-background="new 0 0 15 15" viewBox="0 0 15 15" x="0" y="0" class="shopee-svg-icon 
f3N1Rf icon-down-arrow-filled"><path d="m6.5 12.9-6-7.9s-1.4-1.5.5-1.5h13s1.8 0 .6 1.5l-6 7.9c-.1 0-.9 1.3-2.1 
0z"></path></svg></button></div></div></div></div></section><div class="ArX7yj"><svg fill="none" viewBox="0 -2 23 22" class="shopee-svg-icon lGPe96 
icon-voucher-line"><g filter="url(#voucher-filter0_d)"><mask id="a" fill="#fff"><path fill-rule="evenodd" clip-rule="evenodd" d="M1 2h18v2.32a1.5 
1.5 0 000 2.75v.65a1.5 1.5 0 000 2.75v.65a1.5 1.5 0 000 2.75V16H1v-2.12a1.5 1.5 0 000-2.75v-.65a1.5 1.5 0 000-2.75v-.65a1.5 1.5 0 
000-2.75V2z"></path></mask><path d="M19 2h1V1h-1v1zM1 2V1H0v1h1zm18 2.32l.4.92.6-.26v-.66h-1zm0 2.75h1v-.65l-.6-.26-.4.91zm0 
.65l.4.92.6-.26v-.66h-1zm0 2.75h1v-.65l-.6-.26-.4.91zm0 .65l.4.92.6-.26v-.66h-1zm0 2.75h1v-.65l-.6-.26-.4.91zM19 16v1h1v-1h-1zM1 
16H0v1h1v-1zm0-2.12l-.4-.92-.6.26v.66h1zm0-2.75H0v.65l.6.26.4-.91zm0-.65l-.4-.92-.6.26v.66h1zm0-2.75H0v.65l.6.26.4-.91zm0-.65l-.4-.92-.6.26v
.66h1zm0-2.75H0v.65l.6.26.4-.91zM19 1H1v2h18V1zm1 3.32V2h-2v2.32h2zm-.9 1.38c0-.2.12-.38.3-.46l-.8-1.83a2.5 2.5 0 00-1.5 2.29h2zm.3.46a.5.5 0 
01-.3-.46h-2c0 1.03.62 1.9 1.5 2.3l.8-1.84zm.6 1.56v-.65h-2v.65h2zm-.9 1.38c0-.2.12-.38.3-.46l-.8-1.83a2.5 2.5 0 00-1.5 2.29h2zm.3.46a.5.5 0 
01-.3-.46h-2c0 1.03.62 1.9 1.5 2.3l.8-1.84zm.6 1.56v-.65h-2v.65h2zm-.9 1.38c0-.2.12-.38.3-.46l-.8-1.83a2.5 2.5 0 00-1.5 2.29h2zm.3.46a.5.5 0 
01-.3-.46h-2c0 1.03.62 1.9 1.5 2.3l.8-1.84zM20 16v-2.13h-2V16h2zM1 17h18v-2H1v2zm-1-3.12V16h2v-2.12H0zm1.4.91a2.5 2.5 0 001.5-2.29h-2a.5.5 0 
01-.3.46l.8 1.83zm1.5-2.29a2.5 2.5 0 00-1.5-2.3l-.8 1.84c.18.08.3.26.3.46h2zM0 10.48v.65h2v-.65H0zM.9 9.1a.5.5 0 01-.3.46l.8 1.83A2.5 2.5 0 002.9 
9.1h-2zm-.3-.46c.18.08.3.26.3.46h2a2.5 2.5 0 00-1.5-2.3L.6 8.65zM0 7.08v.65h2v-.65H0zM.9 5.7a.5.5 0 01-.3.46l.8 1.83A2.5 2.5 0 002.9 
5.7h-2zm-.3-.46c.18.08.3.26.3.46h2a2.5 2.5 0 00-1.5-2.3L.6 5.25zM0 2v2.33h2V2H0z" mask="url(#a)"></path></g><path clip-rule="evenodd" d="M6.49 
14.18h.86v-1.6h-.86v1.6zM6.49 11.18h.86v-1.6h-.86v1.6zM6.49 8.18h.86v-1.6h-.86v1.6zM6.49 5.18h.86v-1.6h-.86v1.6z"></path><defs><filter 
id="voucher-filter0_d" x="0" y="1" width="20" height="16" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB"><feFlood 
flood-opacity="0" result="BackgroundImageFix"></feFlood><feColorMatrix in="SourceAlpha" values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 127 
0"></feColorMatrix><feOffset></feOffset><feGaussianBlur stdDeviation=".5"></feGaussianBlur><feColorMatrix values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
0 0.09 0"></feColorMatrix><feBlend in2="BackgroundImageFix" result="effect1_dropShadow"></feBlend><feBlend in="SourceGraphic" 
in2="effect1_dropShadow" result="shape"></feBlend></filter></defs></svg><div class="N9nCmB"><div class="nKTIzW">Up to 15% off voucher 
available</div><div class="JC72Dv"><button class="qe2YoR">More Vouchers</button><div style="display: contents;"></div></div></div></div><div 
class="_RPX38"><img width="20" height="20" src="https://deo.shopeemobile.com/shopee/shopee-pcmall-live-sg/cart/094f639ce7dff28ced5b.png" 
alt="fs-icon"><div class="Cmb29y">Up to RM5.00 off shipping for orders over RM0.00</div><div class="shopee-drawer" id="pc-drawer-id-4" 
tabindex="0"><span class="Eb1Wor" aria-describedby="848739804_shipping_discount"> Learn more </span></div></div></section><section 
class="AuhAvM"><h3 class="a11y-hidden">Shop Section</h3><div class="JsC6Oq"><div class="gzSvrb"><div class="Ll5dDW"><label 
class="stardust-checkbox"><input class="stardust-checkbox__input" type="checkbox" aria-checked="false" tabindex="0" role="checkbox" 
aria-label="Click here to select all products in JCSP"><div class="stardust-checkbox__box"></div></label></div><a class="QcqMX5" 
href="/jasonlaw5511?categoryId=100637&amp;entryPoint=cart&amp;itemId=10546776825"><div class="Koi0Pw"><svg xmlns="http://www.w3.org/2000/svg" 
width="58" height="16" fill="none"><title>Preferred Seller</title><path fill="#EE4D2D" fill-rule="evenodd" d="M0 2C0 .9.9 0 2 0h54a2 2 0 012 2v12a2 
2 0 01-2 2H2a2 2 0 01-2-2V2z" clip-rule="evenodd"></path><path fill="#fff" d="M6.3 9.3v3.2H5V4H8c1 0 1.7.2 2.3.7.6.5.8 1.2.8 2s-.2 1.5-.8 
2c-.5.4-1.3.6-2.3.6H6.3zm0-1.2h1.8c.6 0 1 0 1.2-.3.3-.3.5-.6.5-1.1 0-.5-.2-.8-.5-1.1-.2-.3-.6-.4-1.1-.4H6.3v3zm9.4-.6h-.6c-.6 0-1 
.2-1.3.7v4.3h-1.4V6.2h1.4v.7c.3-.6.8-.9 1.4-.9l.5.1v1.4zm3.6 5.1a3 3 0 01-2.2-.8c-.6-.6-.8-1.4-.8-2.3v-.2c0-.6 0-1.2.3-1.7s.6-.9 1-1.1c.5-.3 1-.5 
1.5-.5.9 0 1.6.3 2 .9.5.5.7 1.3.7 2.3v.6h-4.1c0 .5.2 1 .5 1.2.3.3.7.5 1.2.5a2 2 0 001.6-.8l.7.7c-.2.4-.6.7-1 1l-1.4.2zm-.2-5.4c-.4 0-.7.1-1 .4l-.4 
1.1h2.7c0-.5-.1-.9-.3-1.1-.3-.3-.6-.4-1-.4zm4.4 5.3V7.2h-1v-1h1v-.6c0-.7.1-1.3.5-1.6.4-.4 1-.6 1.7-.6h.8v1.2h-.6c-.7 0-1 .3-1 
1v.6h1.3v1h-1.3v5.3h-1.4zm6.4.1a3 3 0 01-2.2-.8c-.6-.6-.9-1.4-.9-2.3v-.2c0-.6.1-1.2.4-1.7.2-.5.6-.9 1-1.1.5-.3 1-.5 1.5-.5.9 0 1.5.3 2 .9.5.5.7 
1.3.7 2.3v.6h-4.1c0 .5.2 1 .5 1.2.3.3.7.5 1.1.5a2 2 0 001.6-.8l.8.7-1 1-1.4.2zm-.2-5.4c-.4 0-.7.1-1 .4-.2.3-.4.7-.4 
1.1H31c0-.5-.2-.9-.4-1.1-.2-.3-.5-.4-1-.4zm7.1.3h-.5c-.7 0-1.1.2-1.4.7v4.3h-1.4V6.2H35v.7c.3-.6.8-.9 1.4-.9l.5.1v1.4zm4.2 0h-.5c-.7 
0-1.1.2-1.3.7v4.3h-1.5V6.2h1.4v.7c.4-.6.8-.9 1.5-.9l.5.1v1.4zm3.6 5.1a3 3 0 01-2.2-.8c-.5-.6-.8-1.4-.8-2.3v-.2c0-.6.1-1.2.4-1.7.2-.5.5-.9 
1-1.1.4-.3 1-.5 1.5-.5.8 0 1.5.3 2 .9.4.5.7 1.3.7 2.3v.6H43c0 .5.2 1 .5 1.2.4.3.7.5 1.2.5a2 2 0 001.6-.8l.8.7-1 1-1.5.2zm-.1-5.4c-.4 0-.8.1-1 .4L43 
8.7h2.8c0-.5-.2-.9-.4-1.1-.2-.3-.6-.4-1-.4zm3.5 2c0-.9.2-1.7.7-2.3.4-.6 1-.9 1.8-.9a2 2 0 011.6.7V3.5h1.5v9h-1.3v-.7c-.5.6-1 .8-1.8.8-.7 
0-1.3-.3-1.8-.9a4 4 0 01-.7-2.4zm1.4.2c0 .7.2 1.2.4 1.5.3.4.6.6 1 .6.6 0 1-.3 1.3-.8V8c-.2-.5-.6-.8-1.2-.8-.5 0-.8.2-1 .6a3 3 0 00-.5 
1.6z"></path></svg></div><span style="margin-left: 10px;">JCSP</span></a><button class="Eg4UEE"><svg viewBox="0 0 16 16" class="shopee-svg-icon 
AxeMgG"><g fill-rule="evenodd"><path d="M15 4a1 1 0 01.993.883L16 5v9.932a.5.5 0 01-.82.385l-2.061-1.718-8.199.001a1 1 0 
01-.98-.8l-.016-.117-.108-1.284 8.058.001a2 2 0 001.976-1.692l.018-.155L14.293 4H15zm-2.48-4a1 1 0 011 1l-.003.077-.646 8.4a1 1 0 
01-.997.923l-8.994-.001-2.06 1.718a.5.5 0 01-.233.108l-.087.007a.5.5 0 01-.492-.41L0 11.732V1a1 1 0 011-1h11.52zM3.646 4.246a.5.5 0 000 
.708c.305.304.694.526 1.146.682A4.936 4.936 0 006.4 5.9c.464 0 1.02-.062 1.608-.264.452-.156.841-.378 1.146-.682a.5.5 0 
10-.708-.708c-.185.186-.445.335-.764.444a4.004 4.004 0 01-2.564 0c-.319-.11-.579-.258-.764-.444a.5.5 0 00-.708 0z"></path></g></svg></button><div 
class="cVlPY7"></div><div class="p1DEnN"><svg fill="none" viewBox="0 0 18 18" class="shopee-svg-icon KeOYUq icon-coin-line"><path stroke="#FFA600" 
stroke-width="1.3" d="M17.35 9A8.35 8.35 0 11.65 9a8.35 8.35 0 0116.7 0z"></path><path fill="#FFA600" fill-rule="evenodd" stroke="#FFA600" 
stroke-width=".2" d="M6.86 4.723c-.683.576-.998 1.627-.75 2.464.215.725.85 1.258 1.522 1.608.37.193.77.355 
1.177.463.1.027.2.051.3.08.098.03.196.062.294.096.06.021.121.044.182.067.017.006.107.041.04.014-.07-.028.071.03.087.037.286.124.56.27.82.44.114.076
.045.024.151.111a2.942 2.942 0 01.322.303c.087.093.046.042.114.146.18.275.245.478.235.8-.01.328-.14.659-.325.867-.47.53-1.232.73-1.934.696a4.727 
4.727 0 01-1.487-.307c-.45-.182-.852-.462-1.242-.737-.25-.176-.643-.04-.788.197-.17.279-.044.574.207.75.753.532 1.539.946 2.474 1.098.885.144 
1.731.124 2.563-.224.78-.326 1.416-.966 1.607-1.772.198-.838-.023-1.644-.61-2.29-.683-.753-1.722-1.17-2.706-1.43a4.563 4.563 0 
01-.543-.183c.122.048-.044-.02-.078-.035a4.77 4.77 0 01-.422-.212c-.594-.338-.955-.722-.872-1.369.105-.816.757-1.221 1.555-1.28.808-.06 1.648.135 
2.297.554.614.398 1.19-.553.58-.947-1.33-.86-3.504-1.074-4.77-.005z" clip-rule="evenodd"></path></svg>Shopee coins 
redeemable</div></div></div><section class="RqMReY" role="list"><div class="lDiGJB" role="listitem"><h4 
class="a11y-hidden">cart_accessibility_item</h4><div class="f1bSN6"><div class="Xp4RLg"><label class="stardust-checkbox"><input 
class="stardust-checkbox__input" type="checkbox" aria-checked="false" aria-disabled="false" tabindex="0" role="checkbox" aria-label="Click here to 
select this product"><div class="stardust-checkbox__box"></div></label></div><div class="brf29Y"><div class="bzhajK"><a title="🔥Ready Stock🔥14 
in1 Multifunction Push Up Board Training System Fitness Exercise Tools  GYM Body Training Pumping Board" 
href="/🔥Ready-Stock🔥14-in1-Multifunction-Push-Up-Board-Training-System-Fitness-Exercise-Tools-GYM-Body-Training-Pumping-Board-i.18066755
.10546776825?xptdk=b5b2e7c9-eb4b-44fc-a531-4ee19ba8f2ab"><img class="jFEiVQ" 
src="https://down-my.img.susercontent.com/file/f81f7937831482c83d9f306248e709e7" alt="product image"></a><div class="Ou_0WX"><a class="c54pg1" 
title="🔥Ready Stock🔥14 in1 Multifunction Push Up Board Training System Fitness Exercise Tools  GYM Body Training Pumping Board" 
href="/🔥Ready-Stock🔥14-in1-Multifunction-Push-Up-Board-Training-System-Fitness-Exercise-Tools-GYM-Body-Training-Pumping-Board-i.18066755
.10546776825?xptdk=b5b2e7c9-eb4b-44fc-a531-4ee19ba8f2ab">🔥Ready Stock🔥14 in1 Multifunction Push Up Board Training System Fitness Exercise Tools  
GYM Body Training Pumping Board</a><img class="Kv1AvK" src="https://down-my.img.susercontent.com/file/my-50009109-07d26479b71d36d840c404c716d03602
"><div class="gvFc9h"></div></div></div><div class="Jkd76v bzhajK">RM 23.00 on 25 Feb Only</div></div><div class="eHDC_o"></div><div 
class="gJyWia"><div><span class="vjkBXu tnTSPU">RM60.00</span><span class="vjkBXu">RM23.00</span></div></div><div class="sluy3i"><div class="GpmJtT 
shopee-input-quantity"><button class="WNSVcC" aria-label="Decrease"><svg enable-background="new 0 0 10 10" viewBox="0 0 10 10" x="0" y="0" 
class="shopee-svg-icon"><polygon points="4.5 4.5 3.5 4.5 0 4.5 0 5.5 3.5 5.5 4.5 5.5 10 5.5 10 4.5"></polygon></svg></button><input class="WNSVcC 
g2m9n4" type="text" role="spinbutton" aria-valuenow="1" value="1"><button class="WNSVcC" aria-label="Increase"><svg enable-background="new 0 0 10 
10" viewBox="0 0 10 10" x="0" y="0" class="shopee-svg-icon icon-plus-sign"><polygon points="10 4.5 5.5 4.5 5.5 0 4.5 0 4.5 4.5 0 4.5 0 5.5 4.5 5.5 
4.5 10 5.5 10 5.5 5.5 10 5.5"></polygon></svg></button></div></div><div class="HRvCAv"><span>RM23.00</span><span class="a11y-hidden">Total price: 
RM23.00</span></div><div class="bRSn43 TvSDdG"><button class="lSrQtj">Delete</button><div class="J8cCGR"><button class="shopee-button-no-outline 
slfWNx"><span class="wZrjgF">Find Similar</span><svg enable-background="new 0 0 15 15" viewBox="0 0 15 15" x="0" y="0" class="shopee-svg-icon 
f3N1Rf icon-down-arrow-filled"><path d="m6.5 12.9-6-7.9s-1.4-1.5.5-1.5h13s1.8 0 .6 1.5l-6 7.9c-.1 0-.9 1.3-2.1 
0z"></path></svg></button></div></div></div></div></section><div class="_RPX38"><img width="20" height="20" 
src="https://deo.shopeemobile.com/shopee/shopee-pcmall-live-sg/cart/094f639ce7dff28ced5b.png" alt="fs-icon"><div class="Cmb29y">Up to RM5.00 off 
shipping for orders over RM0.00</div><div class="shopee-drawer" id="pc-drawer-id-5" tabindex="0"><span class="Eb1Wor" 
aria-describedby="18066755_shipping_discount"> Learn more </span></div></div></section><section class="AuhAvM"><h3 class="a11y-hidden">Shop 
Section</h3><div class="JsC6Oq"><div class="gzSvrb"><div class="Ll5dDW"><label class="stardust-checkbox"><input class="stardust-checkbox__input" 
type="checkbox" aria-checked="false" tabindex="0" role="checkbox" aria-label="Click here to select all products in YOGA FITNESS SPORTS MALL"><div 
class="stardust-checkbox__box"></div></label></div><a class="QcqMX5" 
href="/sina198888?categoryId=100637&amp;entryPoint=cart&amp;itemId=8039309984"><div><svg width="17" height="16" viewBox="0 0 17 16" 
class="Koi0Pw"><title>Shop Icon</title><path d="M1.95 6.6c.156.804.7 1.867 1.357 1.867.654 0 1.43 0 1.43-.933h.932s0 .933 1.155.933c1.176 0 
1.15-.933 1.15-.933h.984s-.027.933 1.148.933c1.157 0 1.15-.933 1.15-.933h.94s0 .933 1.43.933c1.368 0 1.356-1.867 
1.356-1.867H1.95zm11.49-4.666H3.493L2.248 5.667h12.437L13.44 1.934zM2.853 14.066h11.22l-.01-4.782c-.148.02-.295.042-.465.042-.7 
0-1.436-.324-1.866-.86-.376.53-.88.86-1.622.86-.667 0-1.255-.417-1.64-.86-.39.443-.976.86-1.643.86-.74 
0-1.246-.33-1.623-.86-.43.536-1.195.86-1.895.86-.152 0-.297-.02-.436-.05l-.018 4.79zM14.996 12.2v.933L14.984 15H1.94l-.002-1.867V8.84C1.355 8.306 
1.003 7.456 1 6.6L2.87 1h11.193l1.866 5.6c0 .943-.225 1.876-.934 2.39v3.21z" stroke-width=".3" stroke="#333" fill="#333" 
fill-rule="evenodd"></path></svg></div><span style="margin-left: 10px;">YOGA FITNESS SPORTS MALL</span></a><button class="Eg4UEE"><svg viewBox="0 0 
16 16" class="shopee-svg-icon AxeMgG"><g fill-rule="evenodd"><path d="M15 4a1 1 0 01.993.883L16 5v9.932a.5.5 0 01-.82.385l-2.061-1.718-8.199.001a1 
1 0 01-.98-.8l-.016-.117-.108-1.284 8.058.001a2 2 0 001.976-1.692l.018-.155L14.293 4H15zm-2.48-4a1 1 0 011 1l-.003.077-.646 8.4a1 1 0 
01-.997.923l-8.994-.001-2.06 1.718a.5.5 0 01-.233.108l-.087.007a.5.5 0 01-.492-.41L0 11.732V1a1 1 0 011-1h11.52zM3.646 4.246a.5.5 0 000 
.708c.305.304.694.526 1.146.682A4.936 4.936 0 006.4 5.9c.464 0 1.02-.062 1.608-.264.452-.156.841-.378 1.146-.682a.5.5 0 
10-.708-.708c-.185.186-.445.335-.764.444a4.004 4.004 0 01-2.564 0c-.319-.11-.579-.258-.764-.444a.5.5 0 00-.708 0z"></path></g></svg></button><div 
class="cVlPY7"></div></div></div><section class="RqMReY" role="list"><div class="_9G37m"><div class="wsVAKH"><span 
class="lKqYHD">Bundle</span><span>Any 2 enjoy RM0.30 off</span><span class="Vm8iNU"><a href="/bundle-deal/220894218?from=cart">Add more<svg 
viewBox="0 0 12 12" fill="none" width="12" height="12" color="#ee4d2d" class="MuMxsb"><path fill-rule="evenodd" clip-rule="evenodd" d="M9.293 
6L4.146.854l.708-.708L10 5.293a1 1 0 010 1.414l-5.146 5.147-.708-.707L9.293 6z" fill="currentColor"></path></svg></a></span></div><div 
class="lDiGJB kEMRam" role="listitem"><h4 class="a11y-hidden">cart_accessibility_item</h4><div class="f1bSN6"><div class="Xp4RLg"><label 
class="stardust-checkbox"><input class="stardust-checkbox__input" type="checkbox" aria-checked="false" aria-disabled="false" tabindex="0" 
role="checkbox" aria-label="Click here to select this product"><div class="stardust-checkbox__box"></div></label></div><div class="brf29Y"><div 
class="bzhajK"><a title="1kg/4kg Dumbell Hexagon Dumbbell Gym Fitness Exercise Home Weight Training Workout Neoprene Dumbell" 
href="/1kg-4kg-Dumbell-Hexagon-Dumbbell-Gym-Fitness-Exercise-Home-Weight-Training-Workout-Neoprene-Dumbell-i.256033736.8039309984?xptdk=13a133b0
-b39f-43c3-8c28-4d6a34b77a35"><img class="jFEiVQ" src="https://down-my.img.susercontent.com/file/my-11134207-7r992-lmolaenqj1cm59" alt="product 
image"></a><div class="Ou_0WX"><a class="c54pg1" title="1kg/4kg Dumbell Hexagon Dumbbell Gym Fitness Exercise Home Weight Training Workout Neoprene 
Dumbell" href="/1kg-4kg-Dumbell-Hexagon-Dumbbell-Gym-Fitness-Exercise-Home-Weight-Training-Workout-Neoprene-Dumbell-i.256033736.8039309984?xptdk
=13a133b0-b39f-43c3-8c28-4d6a34b77a35">1kg/4kg Dumbell Hexagon Dumbbell Gym Fitness Exercise Home Weight Training Workout Neoprene Dumbell</a><img 
class="Kv1AvK" src="https://down-my.img.susercontent.com/file/my-50009109-07d26479b71d36d840c404c716d03602"><div 
class="gvFc9h"></div></div></div><div class="Jkd76v bzhajK">RM 26.90 on 25 Feb Only</div></div><div class="eHDC_o"><div class="qNRZqG"><button 
class="mM4TZ8" role="button" tabindex="0"><div class="iIg1CN">Variations:<div class="E33rwr"></div></div><div class="dDPSp3">🔥1pcs Black-(
3kg)</div></button><div></div></div></div><div class="gJyWia"><div><span class="vjkBXu tnTSPU">RM50.00</span><span 
class="vjkBXu">RM26.90</span></div></div><div class="sluy3i"><div class="GpmJtT shopee-input-quantity"><button class="WNSVcC" 
aria-label="Decrease"><svg enable-background="new 0 0 10 10" viewBox="0 0 10 10" x="0" y="0" class="shopee-svg-icon"><polygon points="4.5 4.5 3.5 
4.5 0 4.5 0 5.5 3.5 5.5 4.5 5.5 10 5.5 10 4.5"></polygon></svg></button><input class="WNSVcC g2m9n4" type="text" role="spinbutton" 
aria-valuenow="1" value="1"><button class="WNSVcC" aria-label="Increase"><svg enable-background="new 0 0 10 10" viewBox="0 0 10 10" x="0" y="0" 
class="shopee-svg-icon icon-plus-sign"><polygon points="10 4.5 5.5 4.5 5.5 0 4.5 0 4.5 4.5 0 4.5 0 5.5 4.5 5.5 4.5 10 5.5 10 5.5 5.5 10 
5.5"></polygon></svg></button></div></div><div class="HRvCAv"><span>RM26.90</span><span class="a11y-hidden">Total price: RM26.90</span></div><div 
class="bRSn43 TvSDdG"><button class="lSrQtj">Delete</button><div class="J8cCGR"><button class="shopee-button-no-outline slfWNx"><span 
class="wZrjgF">Find Similar</span><svg enable-background="new 0 0 15 15" viewBox="0 0 15 15" x="0" y="0" class="shopee-svg-icon f3N1Rf 
icon-down-arrow-filled"><path d="m6.5 12.9-6-7.9s-1.4-1.5.5-1.5h13s1.8 0 .6 1.5l-6 7.9c-.1 0-.9 1.3-2.1 
0z"></path></svg></button></div></div></div></div><div class="t89ViJ"></div></div></section><div class="ArX7yj"><svg fill="none" viewBox="0 -2 23 
22" class="shopee-svg-icon lGPe96 icon-voucher-line"><g filter="url(#voucher-filter0_d)"><mask id="a" fill="#fff"><path fill-rule="evenodd" 
clip-rule="evenodd" d="M1 2h18v2.32a1.5 1.5 0 000 2.75v.65a1.5 1.5 0 000 2.75v.65a1.5 1.5 0 000 2.75V16H1v-2.12a1.5 1.5 0 000-2.75v-.65a1.5 1.5 0 
000-2.75v-.65a1.5 1.5 0 000-2.75V2z"></path></mask><path d="M19 2h1V1h-1v1zM1 2V1H0v1h1zm18 2.32l.4.92.6-.26v-.66h-1zm0 
2.75h1v-.65l-.6-.26-.4.91zm0 .65l.4.92.6-.26v-.66h-1zm0 2.75h1v-.65l-.6-.26-.4.91zm0 .65l.4.92.6-.26v-.66h-1zm0 2.75h1v-.65l-.6-.26-.4.91zM19 
16v1h1v-1h-1zM1 16H0v1h1v-1zm0-2.12l-.4-.92-.6.26v.66h1zm0-2.75H0v.65l.6.26.4-.91zm0-.65l-.4-.92-.6.26v.66h1zm0-2.75H0v.65l.6.26.4-.91zm0-.65l-.4
-.92-.6.26v.66h1zm0-2.75H0v.65l.6.26.4-.91zM19 1H1v2h18V1zm1 3.32V2h-2v2.32h2zm-.9 1.38c0-.2.12-.38.3-.46l-.8-1.83a2.5 2.5 0 00-1.5 
2.29h2zm.3.46a.5.5 0 01-.3-.46h-2c0 1.03.62 1.9 1.5 2.3l.8-1.84zm.6 1.56v-.65h-2v.65h2zm-.9 1.38c0-.2.12-.38.3-.46l-.8-1.83a2.5 2.5 0 00-1.5 
2.29h2zm.3.46a.5.5 0 01-.3-.46h-2c0 1.03.62 1.9 1.5 2.3l.8-1.84zm.6 1.56v-.65h-2v.65h2zm-.9 1.38c0-.2.12-.38.3-.46l-.8-1.83a2.5 2.5 0 00-1.5 
2.29h2zm.3.46a.5.5 0 01-.3-.46h-2c0 1.03.62 1.9 1.5 2.3l.8-1.84zM20 16v-2.13h-2V16h2zM1 17h18v-2H1v2zm-1-3.12V16h2v-2.12H0zm1.4.91a2.5 2.5 0 
001.5-2.29h-2a.5.5 0 01-.3.46l.8 1.83zm1.5-2.29a2.5 2.5 0 00-1.5-2.3l-.8 1.84c.18.08.3.26.3.46h2zM0 10.48v.65h2v-.65H0zM.9 9.1a.5.5 0 01-.3.46l.8 
1.83A2.5 2.5 0 002.9 9.1h-2zm-.3-.46c.18.08.3.26.3.46h2a2.5 2.5 0 00-1.5-2.3L.6 8.65zM0 7.08v.65h2v-.65H0zM.9 5.7a.5.5 0 01-.3.46l.8 1.83A2.5 2.5 0 
002.9 5.7h-2zm-.3-.46c.18.08.3.26.3.46h2a2.5 2.5 0 00-1.5-2.3L.6 5.25zM0 2v2.33h2V2H0z" mask="url(#a)"></path></g><path clip-rule="evenodd" 
d="M6.49 14.18h.86v-1.6h-.86v1.6zM6.49 11.18h.86v-1.6h-.86v1.6zM6.49 8.18h.86v-1.6h-.86v1.6zM6.49 5.18h.86v-1.6h-.86v1.6z"></path><defs><filter 
id="voucher-filter0_d" x="0" y="1" width="20" height="16" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB"><feFlood 
flood-opacity="0" result="BackgroundImageFix"></feFlood><feColorMatrix in="SourceAlpha" values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 127 
0"></feColorMatrix><feOffset></feOffset><feGaussianBlur stdDeviation=".5"></feGaussianBlur><feColorMatrix values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
0 0.09 0"></feColorMatrix><feBlend in2="BackgroundImageFix" result="effect1_dropShadow"></feBlend><feBlend in="SourceGraphic" 
in2="effect1_dropShadow" result="shape"></feBlend></filter></defs></svg><div class="N9nCmB"><div class="nKTIzW">Up to RM1.3 off voucher 
available</div><div class="JC72Dv"><button class="qe2YoR">More Vouchers</button><div style="display: contents;"></div></div></div></div><div 
class="_RPX38"><img width="20" height="20" src="https://deo.shopeemobile.com/shopee/shopee-pcmall-live-sg/cart/094f639ce7dff28ced5b.png" 
alt="fs-icon"><div class="Cmb29y">Up to RM5.00 off shipping for orders over RM0.00</div><div class="shopee-drawer" id="pc-drawer-id-6" 
tabindex="0"><span class="Eb1Wor" aria-describedby="256033736_shipping_discount"> Learn more </span></div></div></section><section 
class="AuhAvM"><h3 class="a11y-hidden">Shop Section</h3><div class="JsC6Oq"><div class="gzSvrb"><div class="Ll5dDW"><label 
class="stardust-checkbox"><input class="stardust-checkbox__input" type="checkbox" aria-checked="false" tabindex="0" role="checkbox" 
aria-label="Click here to select all products in Jodiemall"><div class="stardust-checkbox__box"></div></label></div><a class="QcqMX5" 
href="/jodiemall?categoryId=100017&amp;entryPoint=cart&amp;itemId=23757102635"><div><svg width="17" height="16" viewBox="0 0 17 16" 
class="Koi0Pw"><title>Shop Icon</title><path d="M1.95 6.6c.156.804.7 1.867 1.357 1.867.654 0 1.43 0 1.43-.933h.932s0 .933 1.155.933c1.176 0 
1.15-.933 1.15-.933h.984s-.027.933 1.148.933c1.157 0 1.15-.933 1.15-.933h.94s0 .933 1.43.933c1.368 0 1.356-1.867 
1.356-1.867H1.95zm11.49-4.666H3.493L2.248 5.667h12.437L13.44 1.934zM2.853 14.066h11.22l-.01-4.782c-.148.02-.295.042-.465.042-.7 
0-1.436-.324-1.866-.86-.376.53-.88.86-1.622.86-.667 0-1.255-.417-1.64-.86-.39.443-.976.86-1.643.86-.74 
0-1.246-.33-1.623-.86-.43.536-1.195.86-1.895.86-.152 0-.297-.02-.436-.05l-.018 4.79zM14.996 12.2v.933L14.984 15H1.94l-.002-1.867V8.84C1.355 8.306 
1.003 7.456 1 6.6L2.87 1h11.193l1.866 5.6c0 .943-.225 1.876-.934 2.39v3.21z" stroke-width=".3" stroke="#333" fill="#333" 
fill-rule="evenodd"></path></svg></div><span style="margin-left: 10px;">Jodiemall</span></a><button class="Eg4UEE"><svg viewBox="0 0 16 16" 
class="shopee-svg-icon AxeMgG"><g fill-rule="evenodd"><path d="M15 4a1 1 0 01.993.883L16 5v9.932a.5.5 0 01-.82.385l-2.061-1.718-8.199.001a1 1 0 
01-.98-.8l-.016-.117-.108-1.284 8.058.001a2 2 0 001.976-1.692l.018-.155L14.293 4H15zm-2.48-4a1 1 0 011 1l-.003.077-.646 8.4a1 1 0 
01-.997.923l-8.994-.001-2.06 1.718a.5.5 0 01-.233.108l-.087.007a.5.5 0 01-.492-.41L0 11.732V1a1 1 0 011-1h11.52zM3.646 4.246a.5.5 0 000 
.708c.305.304.694.526 1.146.682A4.936 4.936 0 006.4 5.9c.464 0 1.02-.062 1.608-.264.452-.156.841-.378 1.146-.682a.5.5 0 
10-.708-.708c-.185.186-.445.335-.764.444a4.004 4.004 0 01-2.564 0c-.319-.11-.579-.258-.764-.444a.5.5 0 00-.708 0z"></path></g></svg></button><div 
class="cVlPY7"></div></div></div><section class="RqMReY" role="list"><div class="lDiGJB" role="listitem"><h4 
class="a11y-hidden">cart_accessibility_item</h4><div class="f1bSN6"><div class="Xp4RLg"><label class="stardust-checkbox"><input 
class="stardust-checkbox__input" type="checkbox" aria-checked="false" aria-disabled="false" tabindex="0" role="checkbox" aria-label="Click here to 
select this product"><div class="stardust-checkbox__box"></div></label></div><div class="brf29Y"><div class="bzhajK"><a title="[TOP SALE] Push Up 
Bra Adjustable Strap Comfortable Latex Seamless Bra For Women No Steel Ring Bra Sport Underwear" 
href="/-TOP-SALE-Push-Up-Bra-Adjustable-Strap-Comfortable-Latex-Seamless-Bra-For-Women-No-Steel-Ring-Bra-Sport-Underwear-i.973492799.23757102635
?xptdk=73ee253a-6ec4-4dd9-8483-2cb653706e1b"><img class="jFEiVQ" src="https://down-my.img.susercontent.com/file/sg-11134201-7rbk1-lmj2dqs5wdw9ef" 
alt="product image"></a><div class="Ou_0WX"><a class="c54pg1" title="[TOP SALE] Push Up Bra Adjustable Strap Comfortable Latex Seamless Bra For 
Women No Steel Ring Bra Sport Underwear" href="/-TOP-SALE-Push-Up-Bra-Adjustable-Strap-Comfortable-Latex-Seamless-Bra-For-Women-No-Steel-Ring-Bra
-Sport-Underwear-i.973492799.23757102635?xptdk=73ee253a-6ec4-4dd9-8483-2cb653706e1b">[TOP SALE] Push Up Bra Adjustable Strap Comfortable Latex 
Seamless Bra For Women No Steel Ring Bra Sport Underwear</a><img class="Kv1AvK" 
src="https://down-my.img.susercontent.com/file/my-50009109-07d26479b71d36d840c404c716d03602"><div class="gvFc9h"></div></div></div></div><div 
class="eHDC_o"><div class="qNRZqG"><button class="mM4TZ8" role="button" tabindex="0"><div class="iIg1CN">Variations:<div 
class="E33rwr"></div></div><div class="dDPSp3">Black,S</div></button><div></div></div></div><div class="gJyWia"><div><span class="vjkBXu 
tnTSPU">RM29.00</span><span class="vjkBXu">RM9.39</span></div></div><div class="sluy3i"><div class="GpmJtT shopee-input-quantity"><button 
class="WNSVcC" aria-label="Decrease"><svg enable-background="new 0 0 10 10" viewBox="0 0 10 10" x="0" y="0" class="shopee-svg-icon"><polygon 
points="4.5 4.5 3.5 4.5 0 4.5 0 5.5 3.5 5.5 4.5 5.5 10 5.5 10 4.5"></polygon></svg></button><input class="WNSVcC g2m9n4" type="text" 
role="spinbutton" aria-valuenow="1" value="1"><button class="WNSVcC" aria-label="Increase"><svg enable-background="new 0 0 10 10" viewBox="0 0 10 
10" x="0" y="0" class="shopee-svg-icon icon-plus-sign"><polygon points="10 4.5 5.5 4.5 5.5 0 4.5 0 4.5 4.5 0 4.5 0 5.5 4.5 5.5 4.5 10 5.5 10 5.5 
5.5 10 5.5"></polygon></svg></button></div></div><div class="HRvCAv"><span>RM9.39</span><span class="a11y-hidden">Total price: 
RM9.39</span></div><div class="bRSn43 TvSDdG"><button class="lSrQtj">Delete</button><div class="J8cCGR"><button class="shopee-button-no-outline 
slfWNx"><span class="wZrjgF">Find Similar</span><svg enable-background="new 0 0 15 15" viewBox="0 0 15 15" x="0" y="0" class="shopee-svg-icon 
f3N1Rf icon-down-arrow-filled"><path d="m6.5 12.9-6-7.9s-1.4-1.5.5-1.5h13s1.8 0 .6 1.5l-6 7.9c-.1 0-.9 1.3-2.1 
0z"></path></svg></button></div></div></div></div></section><div class="ArX7yj"><svg fill="none" viewBox="0 -2 23 22" class="shopee-svg-icon lGPe96 
icon-voucher-line"><g filter="url(#voucher-filter0_d)"><mask id="a" fill="#fff"><path fill-rule="evenodd" clip-rule="evenodd" d="M1 2h18v2.32a1.5 
1.5 0 000 2.75v.65a1.5 1.5 0 000 2.75v.65a1.5 1.5 0 000 2.75V16H1v-2.12a1.5 1.5 0 000-2.75v-.65a1.5 1.5 0 000-2.75v-.65a1.5 1.5 0 
000-2.75V2z"></path></mask><path d="M19 2h1V1h-1v1zM1 2V1H0v1h1zm18 2.32l.4.92.6-.26v-.66h-1zm0 2.75h1v-.65l-.6-.26-.4.91zm0 
.65l.4.92.6-.26v-.66h-1zm0 2.75h1v-.65l-.6-.26-.4.91zm0 .65l.4.92.6-.26v-.66h-1zm0 2.75h1v-.65l-.6-.26-.4.91zM19 16v1h1v-1h-1zM1 
16H0v1h1v-1zm0-2.12l-.4-.92-.6.26v.66h1zm0-2.75H0v.65l.6.26.4-.91zm0-.65l-.4-.92-.6.26v.66h1zm0-2.75H0v.65l.6.26.4-.91zm0-.65l-.4-.92-.6.26v
.66h1zm0-2.75H0v.65l.6.26.4-.91zM19 1H1v2h18V1zm1 3.32V2h-2v2.32h2zm-.9 1.38c0-.2.12-.38.3-.46l-.8-1.83a2.5 2.5 0 00-1.5 2.29h2zm.3.46a.5.5 0 
01-.3-.46h-2c0 1.03.62 1.9 1.5 2.3l.8-1.84zm.6 1.56v-.65h-2v.65h2zm-.9 1.38c0-.2.12-.38.3-.46l-.8-1.83a2.5 2.5 0 00-1.5 2.29h2zm.3.46a.5.5 0 
01-.3-.46h-2c0 1.03.62 1.9 1.5 2.3l.8-1.84zm.6 1.56v-.65h-2v.65h2zm-.9 1.38c0-.2.12-.38.3-.46l-.8-1.83a2.5 2.5 0 00-1.5 2.29h2zm.3.46a.5.5 0 
01-.3-.46h-2c0 1.03.62 1.9 1.5 2.3l.8-1.84zM20 16v-2.13h-2V16h2zM1 17h18v-2H1v2zm-1-3.12V16h2v-2.12H0zm1.4.91a2.5 2.5 0 001.5-2.29h-2a.5.5 0 
01-.3.46l.8 1.83zm1.5-2.29a2.5 2.5 0 00-1.5-2.3l-.8 1.84c.18.08.3.26.3.46h2zM0 10.48v.65h2v-.65H0zM.9 9.1a.5.5 0 01-.3.46l.8 1.83A2.5 2.5 0 002.9 
9.1h-2zm-.3-.46c.18.08.3.26.3.46h2a2.5 2.5 0 00-1.5-2.3L.6 8.65zM0 7.08v.65h2v-.65H0zM.9 5.7a.5.5 0 01-.3.46l.8 1.83A2.5 2.5 0 002.9 
5.7h-2zm-.3-.46c.18.08.3.26.3.46h2a2.5 2.5 0 00-1.5-2.3L.6 5.25zM0 2v2.33h2V2H0z" mask="url(#a)"></path></g><path clip-rule="evenodd" d="M6.49 
14.18h.86v-1.6h-.86v1.6zM6.49 11.18h.86v-1.6h-.86v1.6zM6.49 8.18h.86v-1.6h-.86v1.6zM6.49 5.18h.86v-1.6h-.86v1.6z"></path><defs><filter 
id="voucher-filter0_d" x="0" y="1" width="20" height="16" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB"><feFlood 
flood-opacity="0" result="BackgroundImageFix"></feFlood><feColorMatrix in="SourceAlpha" values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 127 
0"></feColorMatrix><feOffset></feOffset><feGaussianBlur stdDeviation=".5"></feGaussianBlur><feColorMatrix values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
0 0.09 0"></feColorMatrix><feBlend in2="BackgroundImageFix" result="effect1_dropShadow"></feBlend><feBlend in="SourceGraphic" 
in2="effect1_dropShadow" result="shape"></feBlend></filter></defs></svg><div class="N9nCmB"><div class="nKTIzW">Up to RM3 off voucher 
available</div><div class="JC72Dv"><button class="qe2YoR">More Vouchers</button><div style="display: contents;"></div></div></div></div><div 
class="_RPX38"><img width="20" height="20" src="https://deo.shopeemobile.com/shopee/shopee-pcmall-live-sg/cart/094f639ce7dff28ced5b.png" 
alt="fs-icon"><div class="Cmb29y">Up to RM5.00 off shipping for orders over RM0.00</div><div class="shopee-drawer" id="pc-drawer-id-7" 
tabindex="0"><span class="Eb1Wor" aria-describedby="973492799_shipping_discount"> Learn more </span></div></div></section><section 
class="AuhAvM"><h3 class="a11y-hidden">Shop Section</h3><div class="JsC6Oq"><div class="gzSvrb"><div class="Ll5dDW"><label 
class="stardust-checkbox"><input class="stardust-checkbox__input" type="checkbox" aria-checked="false" tabindex="0" role="checkbox" 
aria-label="Click here to select all products in gifts_style"><div class="stardust-checkbox__box"></div></label></div><a class="QcqMX5" 
href="/happyrainbow83?categoryId=100017&amp;entryPoint=cart&amp;itemId=23171029710"><div><svg width="17" height="16" viewBox="0 0 17 16" 
class="Koi0Pw"><title>Shop Icon</title><path d="M1.95 6.6c.156.804.7 1.867 1.357 1.867.654 0 1.43 0 1.43-.933h.932s0 .933 1.155.933c1.176 0 
1.15-.933 1.15-.933h.984s-.027.933 1.148.933c1.157 0 1.15-.933 1.15-.933h.94s0 .933 1.43.933c1.368 0 1.356-1.867 
1.356-1.867H1.95zm11.49-4.666H3.493L2.248 5.667h12.437L13.44 1.934zM2.853 14.066h11.22l-.01-4.782c-.148.02-.295.042-.465.042-.7 
0-1.436-.324-1.866-.86-.376.53-.88.86-1.622.86-.667 0-1.255-.417-1.64-.86-.39.443-.976.86-1.643.86-.74 
0-1.246-.33-1.623-.86-.43.536-1.195.86-1.895.86-.152 0-.297-.02-.436-.05l-.018 4.79zM14.996 12.2v.933L14.984 15H1.94l-.002-1.867V8.84C1.355 8.306 
1.003 7.456 1 6.6L2.87 1h11.193l1.866 5.6c0 .943-.225 1.876-.934 2.39v3.21z" stroke-width=".3" stroke="#333" fill="#333" 
fill-rule="evenodd"></path></svg></div><span style="margin-left: 10px;">gifts_style</span></a><button class="Eg4UEE"><svg viewBox="0 0 16 16" 
class="shopee-svg-icon AxeMgG"><g fill-rule="evenodd"><path d="M15 4a1 1 0 01.993.883L16 5v9.932a.5.5 0 01-.82.385l-2.061-1.718-8.199.001a1 1 0 
01-.98-.8l-.016-.117-.108-1.284 8.058.001a2 2 0 001.976-1.692l.018-.155L14.293 4H15zm-2.48-4a1 1 0 011 1l-.003.077-.646 8.4a1 1 0 
01-.997.923l-8.994-.001-2.06 1.718a.5.5 0 01-.233.108l-.087.007a.5.5 0 01-.492-.41L0 11.732V1a1 1 0 011-1h11.52zM3.646 4.246a.5.5 0 000 
.708c.305.304.694.526 1.146.682A4.936 4.936 0 006.4 5.9c.464 0 1.02-.062 1.608-.264.452-.156.841-.378 1.146-.682a.5.5 0 
10-.708-.708c-.185.186-.445.335-.764.444a4.004 4.004 0 01-2.564 0c-.319-.11-.579-.258-.764-.444a.5.5 0 00-.708 0z"></path></g></svg></button><div 
class="cVlPY7"></div></div></div><section class="RqMReY" role="list"><div class="lDiGJB" role="listitem"><h4 
class="a11y-hidden">cart_accessibility_item</h4><div class="f1bSN6"><div class="Xp4RLg"><label class="stardust-checkbox"><input 
class="stardust-checkbox__input" type="checkbox" aria-checked="false" aria-disabled="false" tabindex="0" role="checkbox" aria-label="Click here to 
select this product"><div class="stardust-checkbox__box"></div></label></div><div class="brf29Y"><div class="bzhajK"><a title="#Malsysia Ready 
Stock  IceSilk Thai Latex Bra Gathering Ice Silk Seamless Sports Vest Style 泰国乳胶 M-XXL" 
href="/-Malsysia-Ready-Stock-IceSilk-Thai-Latex-Bra-Gathering-Ice-Silk-Seamless-Sports-Vest-Style-泰国乳胶-M-XXL-i.256734574.23171029710?xptdk=99cf2da3
-9b8b-4bee-b995-9ad232b5a302"><img class="jFEiVQ" src="https://down-my.img.susercontent.com/file/my-11134207-7qul5-ljcy4pfahm5f32" alt="product 
image"></a><div class="Ou_0WX"><a class="c54pg1" title="#Malsysia Ready Stock  IceSilk Thai Latex Bra Gathering Ice Silk Seamless Sports Vest Style 
泰国乳胶 M-XXL" href="/-Malsysia-Ready-Stock-IceSilk-Thai-Latex-Bra-Gathering-Ice-Silk-Seamless-Sports-Vest-Style-泰国乳胶-M-XXL-i.256734574.23171029710
?xptdk=99cf2da3-9b8b-4bee-b995-9ad232b5a302">#Malsysia Ready Stock  IceSilk Thai Latex Bra Gathering Ice Silk Seamless Sports Vest Style 泰国乳胶 
M-XXL</a><img class="Kv1AvK" src="https://down-my.img.susercontent.com/file/my-50009109-07d26479b71d36d840c404c716d03602"><div 
class="gvFc9h"></div></div></div></div><div class="eHDC_o"><div class="qNRZqG"><button class="mM4TZ8" role="button" tabindex="0"><div 
class="iIg1CN">Variations:<div class="E33rwr"></div></div><div class="dDPSp3">Grey,M</div></button><div></div></div></div><div 
class="gJyWia"><div><span class="vjkBXu">RM19.90</span></div></div><div class="sluy3i"><div class="GpmJtT shopee-input-quantity"><button 
class="WNSVcC" aria-label="Decrease"><svg enable-background="new 0 0 10 10" viewBox="0 0 10 10" x="0" y="0" class="shopee-svg-icon"><polygon 
points="4.5 4.5 3.5 4.5 0 4.5 0 5.5 3.5 5.5 4.5 5.5 10 5.5 10 4.5"></polygon></svg></button><input class="WNSVcC g2m9n4" type="text" 
role="spinbutton" aria-valuenow="1" value="1"><button class="WNSVcC" aria-label="Increase"><svg enable-background="new 0 0 10 10" viewBox="0 0 10 
10" x="0" y="0" class="shopee-svg-icon icon-plus-sign"><polygon points="10 4.5 5.5 4.5 5.5 0 4.5 0 4.5 4.5 0 4.5 0 5.5 4.5 5.5 4.5 10 5.5 10 5.5 
5.5 10 5.5"></polygon></svg></button></div><div class="PwuHYD">4 items left</div></div><div class="HRvCAv"><span>RM19.90</span><span 
class="a11y-hidden">Total price: RM19.90</span></div><div class="bRSn43 TvSDdG"><button class="lSrQtj">Delete</button><div class="J8cCGR"><button 
class="shopee-button-no-outline slfWNx"><span class="wZrjgF">Find Similar</span><svg enable-background="new 0 0 15 15" viewBox="0 0 15 15" x="0" 
y="0" class="shopee-svg-icon f3N1Rf icon-down-arrow-filled"><path d="m6.5 12.9-6-7.9s-1.4-1.5.5-1.5h13s1.8 0 .6 1.5l-6 7.9c-.1 0-.9 1.3-2.1 
0z"></path></svg></button></div></div></div></div></section><div class="_RPX38"><img width="20" height="20" 
src="https://deo.shopeemobile.com/shopee/shopee-pcmall-live-sg/cart/094f639ce7dff28ced5b.png" alt="fs-icon"><div class="Cmb29y">Up to RM5.00 off 
shipping for orders over RM0.00</div><div class="shopee-drawer" id="pc-drawer-id-8" tabindex="0"><span class="Eb1Wor" 
aria-describedby="256734574_shipping_discount"> Learn more </span></div></div></section><section class="AuhAvM"><h3 class="a11y-hidden">Shop 
Section</h3><div class="JsC6Oq"><div class="gzSvrb"><div class="Ll5dDW"><label class="stardust-checkbox"><input class="stardust-checkbox__input" 
type="checkbox" aria-checked="false" tabindex="0" role="checkbox" aria-label="Click here to select all products in Onenine.my"><div 
class="stardust-checkbox__box"></div></label></div><a class="QcqMX5" 
href="/onenine.my?categoryId=100017&amp;entryPoint=cart&amp;itemId=18795949744"><div class="Koi0Pw"><svg xmlns="http://www.w3.org/2000/svg" 
width="58" height="16" fill="none"><title>Preferred Seller</title><path fill="#EE4D2D" fill-rule="evenodd" d="M0 2C0 .9.9 0 2 0h54a2 2 0 012 2v12a2 
2 0 01-2 2H2a2 2 0 01-2-2V2z" clip-rule="evenodd"></path><path fill="#fff" d="M6.3 9.3v3.2H5V4H8c1 0 1.7.2 2.3.7.6.5.8 1.2.8 2s-.2 1.5-.8 
2c-.5.4-1.3.6-2.3.6H6.3zm0-1.2h1.8c.6 0 1 0 1.2-.3.3-.3.5-.6.5-1.1 0-.5-.2-.8-.5-1.1-.2-.3-.6-.4-1.1-.4H6.3v3zm9.4-.6h-.6c-.6 0-1 
.2-1.3.7v4.3h-1.4V6.2h1.4v.7c.3-.6.8-.9 1.4-.9l.5.1v1.4zm3.6 5.1a3 3 0 01-2.2-.8c-.6-.6-.8-1.4-.8-2.3v-.2c0-.6 0-1.2.3-1.7s.6-.9 1-1.1c.5-.3 1-.5 
1.5-.5.9 0 1.6.3 2 .9.5.5.7 1.3.7 2.3v.6h-4.1c0 .5.2 1 .5 1.2.3.3.7.5 1.2.5a2 2 0 001.6-.8l.7.7c-.2.4-.6.7-1 1l-1.4.2zm-.2-5.4c-.4 0-.7.1-1 .4l-.4 
1.1h2.7c0-.5-.1-.9-.3-1.1-.3-.3-.6-.4-1-.4zm4.4 5.3V7.2h-1v-1h1v-.6c0-.7.1-1.3.5-1.6.4-.4 1-.6 1.7-.6h.8v1.2h-.6c-.7 0-1 .3-1 
1v.6h1.3v1h-1.3v5.3h-1.4zm6.4.1a3 3 0 01-2.2-.8c-.6-.6-.9-1.4-.9-2.3v-.2c0-.6.1-1.2.4-1.7.2-.5.6-.9 1-1.1.5-.3 1-.5 1.5-.5.9 0 1.5.3 2 .9.5.5.7 
1.3.7 2.3v.6h-4.1c0 .5.2 1 .5 1.2.3.3.7.5 1.1.5a2 2 0 001.6-.8l.8.7-1 1-1.4.2zm-.2-5.4c-.4 0-.7.1-1 .4-.2.3-.4.7-.4 
1.1H31c0-.5-.2-.9-.4-1.1-.2-.3-.5-.4-1-.4zm7.1.3h-.5c-.7 0-1.1.2-1.4.7v4.3h-1.4V6.2H35v.7c.3-.6.8-.9 1.4-.9l.5.1v1.4zm4.2 0h-.5c-.7 
0-1.1.2-1.3.7v4.3h-1.5V6.2h1.4v.7c.4-.6.8-.9 1.5-.9l.5.1v1.4zm3.6 5.1a3 3 0 01-2.2-.8c-.5-.6-.8-1.4-.8-2.3v-.2c0-.6.1-1.2.4-1.7.2-.5.5-.9 
1-1.1.4-.3 1-.5 1.5-.5.8 0 1.5.3 2 .9.4.5.7 1.3.7 2.3v.6H43c0 .5.2 1 .5 1.2.4.3.7.5 1.2.5a2 2 0 001.6-.8l.8.7-1 1-1.5.2zm-.1-5.4c-.4 0-.8.1-1 .4L43 
8.7h2.8c0-.5-.2-.9-.4-1.1-.2-.3-.6-.4-1-.4zm3.5 2c0-.9.2-1.7.7-2.3.4-.6 1-.9 1.8-.9a2 2 0 011.6.7V3.5h1.5v9h-1.3v-.7c-.5.6-1 .8-1.8.8-.7 
0-1.3-.3-1.8-.9a4 4 0 01-.7-2.4zm1.4.2c0 .7.2 1.2.4 1.5.3.4.6.6 1 .6.6 0 1-.3 1.3-.8V8c-.2-.5-.6-.8-1.2-.8-.5 0-.8.2-1 .6a3 3 0 00-.5 
1.6z"></path></svg></div><span style="margin-left: 10px;">Onenine.my</span></a><button class="Eg4UEE"><svg viewBox="0 0 16 16" 
class="shopee-svg-icon AxeMgG"><g fill-rule="evenodd"><path d="M15 4a1 1 0 01.993.883L16 5v9.932a.5.5 0 01-.82.385l-2.061-1.718-8.199.001a1 1 0 
01-.98-.8l-.016-.117-.108-1.284 8.058.001a2 2 0 001.976-1.692l.018-.155L14.293 4H15zm-2.48-4a1 1 0 011 1l-.003.077-.646 8.4a1 1 0 
01-.997.923l-8.994-.001-2.06 1.718a.5.5 0 01-.233.108l-.087.007a.5.5 0 01-.492-.41L0 11.732V1a1 1 0 011-1h11.52zM3.646 4.246a.5.5 0 000 
.708c.305.304.694.526 1.146.682A4.936 4.936 0 006.4 5.9c.464 0 1.02-.062 1.608-.264.452-.156.841-.378 1.146-.682a.5.5 0 
10-.708-.708c-.185.186-.445.335-.764.444a4.004 4.004 0 01-2.564 0c-.319-.11-.579-.258-.764-.444a.5.5 0 00-.708 0z"></path></g></svg></button><div 
class="cVlPY7"></div><div class="p1DEnN"><svg fill="none" viewBox="0 0 18 18" class="shopee-svg-icon KeOYUq icon-coin-line"><path stroke="#FFA600" 
stroke-width="1.3" d="M17.35 9A8.35 8.35 0 11.65 9a8.35 8.35 0 0116.7 0z"></path><path fill="#FFA600" fill-rule="evenodd" stroke="#FFA600" 
stroke-width=".2" d="M6.86 4.723c-.683.576-.998 1.627-.75 2.464.215.725.85 1.258 1.522 1.608.37.193.77.355 
1.177.463.1.027.2.051.3.08.098.03.196.062.294.096.06.021.121.044.182.067.017.006.107.041.04.014-.07-.028.071.03.087.037.286.124.56.27.82.44.114.076
.045.024.151.111a2.942 2.942 0 01.322.303c.087.093.046.042.114.146.18.275.245.478.235.8-.01.328-.14.659-.325.867-.47.53-1.232.73-1.934.696a4.727 
4.727 0 01-1.487-.307c-.45-.182-.852-.462-1.242-.737-.25-.176-.643-.04-.788.197-.17.279-.044.574.207.75.753.532 1.539.946 2.474 1.098.885.144 
1.731.124 2.563-.224.78-.326 1.416-.966 1.607-1.772.198-.838-.023-1.644-.61-2.29-.683-.753-1.722-1.17-2.706-1.43a4.563 4.563 0 
01-.543-.183c.122.048-.044-.02-.078-.035a4.77 4.77 0 01-.422-.212c-.594-.338-.955-.722-.872-1.369.105-.816.757-1.221 1.555-1.28.808-.06 1.648.135 
2.297.554.614.398 1.19-.553.58-.947-1.33-.86-3.504-1.074-4.77-.005z" clip-rule="evenodd"></path></svg>Shopee coins 
redeemable</div></div></div><section class="RqMReY" role="list"><div class="_9G37m"><div class="wsVAKH"><span class="lKqYHD">Bundle</span><span>Any 
2 enjoy 2% off</span><span class="Vm8iNU"><a href="/bundle-deal/221669440?from=cart">Add more<svg viewBox="0 0 12 12" fill="none" width="12" 
height="12" color="#ee4d2d" class="MuMxsb"><path fill-rule="evenodd" clip-rule="evenodd" d="M9.293 6L4.146.854l.708-.708L10 5.293a1 1 0 010 
1.414l-5.146 5.147-.708-.707L9.293 6z" fill="currentColor"></path></svg></a></span></div><div class="lDiGJB kEMRam" role="listitem"><h4 
class="a11y-hidden">cart_accessibility_item</h4><div class="f1bSN6"><div class="Xp4RLg"><label class="stardust-checkbox"><input 
class="stardust-checkbox__input" type="checkbox" aria-checked="false" aria-disabled="false" tabindex="0" role="checkbox" aria-label="Click here to 
select this product"><div class="stardust-checkbox__box"></div></label></div><div class="brf29Y"><div class="bzhajK"><a title="Japanese Seamless 
Bra Square Collar Wireless Bra Suji For Women Push up Plus Size Bra Non wired Underwear" 
href="/Japanese-Seamless-Bra-Square-Collar-Wireless-Bra-Suji-For-Women-Push-up-Plus-Size-Bra-Non-wired-Underwear-i.1142056474.18795949744?xptdk
=b2a09e66-e112-4d54-bdb3-a1aeb00d343a"><img class="jFEiVQ" src="https://down-my.img.susercontent.com/file/sg-11134201-7rblc-loi2ho7x2ub496" 
alt="product image"></a><div class="Ou_0WX"><a class="c54pg1" title="Japanese Seamless Bra Square Collar Wireless Bra Suji For Women Push up Plus 
Size Bra Non wired Underwear" href="/Japanese-Seamless-Bra-Square-Collar-Wireless-Bra-Suji-For-Women-Push-up-Plus-Size-Bra-Non-wired-Underwear-i
.1142056474.18795949744?xptdk=b2a09e66-e112-4d54-bdb3-a1aeb00d343a">Japanese Seamless Bra Square Collar Wireless Bra Suji For Women Push up Plus 
Size Bra Non wired Underwear</a><img class="Kv1AvK" src="https://down-my.img.susercontent.com/file/my-50009109-07d26479b71d36d840c404c716d03602
"><div class="gvFc9h"></div></div></div></div><div class="eHDC_o"><div class="qNRZqG"><button class="mM4TZ8" role="button" tabindex="0"><div 
class="iIg1CN">Variations:<div class="E33rwr"></div></div><div class="dDPSp3">PURPLE,S/32/70/ABC</div></button><div></div></div></div><div 
class="gJyWia"><div><span class="vjkBXu tnTSPU">RM20.90</span><span class="vjkBXu">RM9.90</span></div></div><div class="sluy3i"><div class="GpmJtT 
shopee-input-quantity"><button class="WNSVcC" aria-label="Decrease"><svg enable-background="new 0 0 10 10" viewBox="0 0 10 10" x="0" y="0" 
class="shopee-svg-icon"><polygon points="4.5 4.5 3.5 4.5 0 4.5 0 5.5 3.5 5.5 4.5 5.5 10 5.5 10 4.5"></polygon></svg></button><input class="WNSVcC 
g2m9n4" type="text" role="spinbutton" aria-valuenow="1" value="1"><button class="WNSVcC" aria-label="Increase"><svg enable-background="new 0 0 10 
10" viewBox="0 0 10 10" x="0" y="0" class="shopee-svg-icon icon-plus-sign"><polygon points="10 4.5 5.5 4.5 5.5 0 4.5 0 4.5 4.5 0 4.5 0 5.5 4.5 5.5 
4.5 10 5.5 10 5.5 5.5 10 5.5"></polygon></svg></button></div></div><div class="HRvCAv"><span>RM9.90</span><span class="a11y-hidden">Total price: 
RM9.90</span></div><div class="bRSn43 TvSDdG"><button class="lSrQtj">Delete</button><div class="J8cCGR"><button class="shopee-button-no-outline 
slfWNx"><span class="wZrjgF">Find Similar</span><svg enable-background="new 0 0 15 15" viewBox="0 0 15 15" x="0" y="0" class="shopee-svg-icon 
f3N1Rf icon-down-arrow-filled"><path d="m6.5 12.9-6-7.9s-1.4-1.5.5-1.5h13s1.8 0 .6 1.5l-6 7.9c-.1 0-.9 1.3-2.1 
0z"></path></svg></button></div></div></div></div><div class="t89ViJ"></div></div></section><div class="ArX7yj"><svg fill="none" viewBox="0 -2 23 
22" class="shopee-svg-icon lGPe96 icon-voucher-line"><g filter="url(#voucher-filter0_d)"><mask id="a" fill="#fff"><path fill-rule="evenodd" 
clip-rule="evenodd" d="M1 2h18v2.32a1.5 1.5 0 000 2.75v.65a1.5 1.5 0 000 2.75v.65a1.5 1.5 0 000 2.75V16H1v-2.12a1.5 1.5 0 000-2.75v-.65a1.5 1.5 0 
000-2.75v-.65a1.5 1.5 0 000-2.75V2z"></path></mask><path d="M19 2h1V1h-1v1zM1 2V1H0v1h1zm18 2.32l.4.92.6-.26v-.66h-1zm0 
2.75h1v-.65l-.6-.26-.4.91zm0 .65l.4.92.6-.26v-.66h-1zm0 2.75h1v-.65l-.6-.26-.4.91zm0 .65l.4.92.6-.26v-.66h-1zm0 2.75h1v-.65l-.6-.26-.4.91zM19 
16v1h1v-1h-1zM1 16H0v1h1v-1zm0-2.12l-.4-.92-.6.26v.66h1zm0-2.75H0v.65l.6.26.4-.91zm0-.65l-.4-.92-.6.26v.66h1zm0-2.75H0v.65l.6.26.4-.91zm0-.65l-.4
-.92-.6.26v.66h1zm0-2.75H0v.65l.6.26.4-.91zM19 1H1v2h18V1zm1 3.32V2h-2v2.32h2zm-.9 1.38c0-.2.12-.38.3-.46l-.8-1.83a2.5 2.5 0 00-1.5 
2.29h2zm.3.46a.5.5 0 01-.3-.46h-2c0 1.03.62 1.9 1.5 2.3l.8-1.84zm.6 1.56v-.65h-2v.65h2zm-.9 1.38c0-.2.12-.38.3-.46l-.8-1.83a2.5 2.5 0 00-1.5 
2.29h2zm.3.46a.5.5 0 01-.3-.46h-2c0 1.03.62 1.9 1.5 2.3l.8-1.84zm.6 1.56v-.65h-2v.65h2zm-.9 1.38c0-.2.12-.38.3-.46l-.8-1.83a2.5 2.5 0 00-1.5 
2.29h2zm.3.46a.5.5 0 01-.3-.46h-2c0 1.03.62 1.9 1.5 2.3l.8-1.84zM20 16v-2.13h-2V16h2zM1 17h18v-2H1v2zm-1-3.12V16h2v-2.12H0zm1.4.91a2.5 2.5 0 
001.5-2.29h-2a.5.5 0 01-.3.46l.8 1.83zm1.5-2.29a2.5 2.5 0 00-1.5-2.3l-.8 1.84c.18.08.3.26.3.46h2zM0 10.48v.65h2v-.65H0zM.9 9.1a.5.5 0 01-.3.46l.8 
1.83A2.5 2.5 0 002.9 9.1h-2zm-.3-.46c.18.08.3.26.3.46h2a2.5 2.5 0 00-1.5-2.3L.6 8.65zM0 7.08v.65h2v-.65H0zM.9 5.7a.5.5 0 01-.3.46l.8 1.83A2.5 2.5 0 
002.9 5.7h-2zm-.3-.46c.18.08.3.26.3.46h2a2.5 2.5 0 00-1.5-2.3L.6 5.25zM0 2v2.33h2V2H0z" mask="url(#a)"></path></g><path clip-rule="evenodd" 
d="M6.49 14.18h.86v-1.6h-.86v1.6zM6.49 11.18h.86v-1.6h-.86v1.6zM6.49 8.18h.86v-1.6h-.86v1.6zM6.49 5.18h.86v-1.6h-.86v1.6z"></path><defs><filter 
id="voucher-filter0_d" x="0" y="1" width="20" height="16" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB"><feFlood 
flood-opacity="0" result="BackgroundImageFix"></feFlood><feColorMatrix in="SourceAlpha" values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 127 
0"></feColorMatrix><feOffset></feOffset><feGaussianBlur stdDeviation=".5"></feGaussianBlur><feColorMatrix values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
0 0.09 0"></feColorMatrix><feBlend in2="BackgroundImageFix" result="effect1_dropShadow"></feBlend><feBlend in="SourceGraphic" 
in2="effect1_dropShadow" result="shape"></feBlend></filter></defs></svg><div class="N9nCmB"><div class="nKTIzW">Up to RM6 off voucher 
available</div><div class="JC72Dv"><button class="qe2YoR">More Vouchers</button><div style="display: contents;"></div></div></div></div><div 
class="_RPX38"><img width="20" height="20" src="https://deo.shopeemobile.com/shopee/shopee-pcmall-live-sg/cart/094f639ce7dff28ced5b.png" 
alt="fs-icon"><div class="Cmb29y">Up to RM5.00 off shipping for orders over RM15.00</div><div class="shopee-drawer" id="pc-drawer-id-9" 
tabindex="0"><span class="Eb1Wor" aria-describedby="1142056474_shipping_discount"> Learn more </span></div></div></section><section 
class="AuhAvM"><h3 class="a11y-hidden">Shop Section</h3><div class="JsC6Oq"><div class="gzSvrb"><div class="Ll5dDW"><label 
class="stardust-checkbox"><input class="stardust-checkbox__input" type="checkbox" aria-checked="false" tabindex="0" role="checkbox" 
aria-label="Click here to select all products in uucorner"><div class="stardust-checkbox__box"></div></label></div><a class="QcqMX5" 
href="/uucorner?categoryId=100017&amp;entryPoint=cart&amp;itemId=17063557923"><div class="Koi0Pw"><svg xmlns="http://www.w3.org/2000/svg" 
width="64" height="16" fill="none"><title>Preferred Seller Plus</title><path fill="#EE4D2D" fill-rule="evenodd" d="M0 2C0 .9.9 0 2 0h60a2 2 0 012 
2v12a2 2 0 01-2 2H2a2 2 0 01-2-2V2z" clip-rule="evenodd"></path><path fill="#fff" d="M6.3 9.3v3.2H5V4H8c1 0 1.7.2 2.3.7.6.5.8 1.2.8 2s-.2 1.5-.8 
2c-.5.4-1.3.6-2.3.6H6.3zm0-1.2h1.8c.6 0 1 0 1.2-.3.3-.3.5-.6.5-1.1 0-.5-.2-.8-.5-1.1-.2-.3-.6-.4-1.1-.4H6.3v3zm9.4-.6h-.6c-.6 0-1 
.2-1.3.7v4.3h-1.4V6.2h1.4v.7c.3-.6.8-.9 1.4-.9l.5.1v1.4zm3.6 5.1a3 3 0 01-2.2-.8c-.6-.6-.8-1.4-.8-2.3v-.2c0-.6 0-1.2.3-1.7s.6-.9 1-1.1c.5-.3 1-.5 
1.5-.5.9 0 1.6.3 2 .9.5.5.7 1.3.7 2.3v.6h-4.1c0 .5.2 1 .5 1.2.3.3.7.5 1.2.5a2 2 0 001.6-.8l.7.7c-.2.4-.6.7-1 1l-1.4.2zm-.2-5.4c-.4 0-.7.1-1 .4l-.4 
1.1h2.7c0-.5-.1-.9-.3-1.1-.3-.3-.6-.4-1-.4zm4.4 5.3V7.2h-1v-1h1v-.6c0-.7.1-1.3.5-1.6.4-.4 1-.6 1.7-.6h.8v1.2h-.6c-.7 0-1 .3-1 
1v.6h1.3v1h-1.3v5.3h-1.4zm6.4.1a3 3 0 01-2.2-.8c-.6-.6-.9-1.4-.9-2.3v-.2c0-.6.1-1.2.4-1.7.2-.5.6-.9 1-1.1.5-.3 1-.5 1.5-.5.9 0 1.5.3 2 .9.5.5.7 
1.3.7 2.3v.6h-4.1c0 .5.2 1 .5 1.2.3.3.7.5 1.1.5a2 2 0 001.6-.8l.8.7-1 1-1.4.2zm-.2-5.4c-.4 0-.7.1-1 .4-.2.3-.4.7-.4 
1.1H31c0-.5-.2-.9-.4-1.1-.2-.3-.5-.4-1-.4zm7.1.3h-.5c-.7 0-1.1.2-1.4.7v4.3h-1.4V6.2H35v.7c.3-.6.8-.9 1.4-.9l.5.1v1.4zm4.2 0h-.5c-.7 
0-1.1.2-1.3.7v4.3h-1.5V6.2h1.4v.7c.4-.6.8-.9 1.5-.9l.5.1v1.4zm3.6 5.1a3 3 0 01-2.2-.8c-.5-.6-.8-1.4-.8-2.3v-.2c0-.6.1-1.2.4-1.7.2-.5.5-.9 
1-1.1.4-.3 1-.5 1.5-.5.8 0 1.5.3 2 .9.4.5.7 1.3.7 2.3v.6H43c0 .5.2 1 .5 1.2.4.3.7.5 1.2.5a2 2 0 001.6-.8l.8.7-1 1-1.5.2zm-.1-5.4c-.4 0-.8.1-1 .4L43 
8.7h2.8c0-.5-.2-.9-.4-1.1-.2-.3-.6-.4-1-.4zm3.5 2c0-.9.2-1.7.7-2.3.4-.6 1-.9 1.8-.9a2 2 0 011.6.7V3.5h1.5v9h-1.3v-.7c-.5.6-1 .8-1.8.8-.7 
0-1.3-.3-1.8-.9a4 4 0 01-.7-2.4zm1.4.2c0 .7.2 1.2.4 1.5.3.4.6.6 1 .6.6 0 1-.3 1.3-.8V8c-.2-.5-.6-.8-1.2-.8-.5 0-.8.2-1 .6a3 3 0 00-.5 
1.6z"></path><g clip-path="url(#clip0)"><path fill="#fff" d="M58 8.2h2.2v1.6H58V12h-1.6V9.8h-2.2V8.2h2.2V6H58v2.3z"></path></g><defs><clipPath 
id="clip0"><path fill="#fff" d="M0 0h7v16H0z" transform="translate(54)"></path></clipPath></defs></svg></div><span style="margin-left: 
10px;">uucorner</span></a><button class="Eg4UEE"><svg viewBox="0 0 16 16" class="shopee-svg-icon AxeMgG"><g fill-rule="evenodd"><path d="M15 4a1 1 
0 01.993.883L16 5v9.932a.5.5 0 01-.82.385l-2.061-1.718-8.199.001a1 1 0 01-.98-.8l-.016-.117-.108-1.284 8.058.001a2 2 0 
001.976-1.692l.018-.155L14.293 4H15zm-2.48-4a1 1 0 011 1l-.003.077-.646 8.4a1 1 0 01-.997.923l-8.994-.001-2.06 1.718a.5.5 0 
01-.233.108l-.087.007a.5.5 0 01-.492-.41L0 11.732V1a1 1 0 011-1h11.52zM3.646 4.246a.5.5 0 000 .708c.305.304.694.526 1.146.682A4.936 4.936 0 006.4 
5.9c.464 0 1.02-.062 1.608-.264.452-.156.841-.378 1.146-.682a.5.5 0 10-.708-.708c-.185.186-.445.335-.764.444a4.004 4.004 0 01-2.564 
0c-.319-.11-.579-.258-.764-.444a.5.5 0 00-.708 0z"></path></g></svg></button><div class="cVlPY7"></div><div class="p1DEnN"><svg fill="none" 
viewBox="0 0 18 18" class="shopee-svg-icon KeOYUq icon-coin-line"><path stroke="#FFA600" stroke-width="1.3" d="M17.35 9A8.35 8.35 0 11.65 9a8.35 
8.35 0 0116.7 0z"></path><path fill="#FFA600" fill-rule="evenodd" stroke="#FFA600" stroke-width=".2" d="M6.86 4.723c-.683.576-.998 1.627-.75 
2.464.215.725.85 1.258 1.522 1.608.37.193.77.355 1.177.463.1.027.2.051.3.08.098.03.196.062.294.096.06.021.121.044.182.067.017.006.107.041.04.014
-.07-.028.071.03.087.037.286.124.56.27.82.44.114.076.045.024.151.111a2.942 2.942 0 
01.322.303c.087.093.046.042.114.146.18.275.245.478.235.8-.01.328-.14.659-.325.867-.47.53-1.232.73-1.934.696a4.727 4.727 0 
01-1.487-.307c-.45-.182-.852-.462-1.242-.737-.25-.176-.643-.04-.788.197-.17.279-.044.574.207.75.753.532 1.539.946 2.474 1.098.885.144 1.731.124 
2.563-.224.78-.326 1.416-.966 1.607-1.772.198-.838-.023-1.644-.61-2.29-.683-.753-1.722-1.17-2.706-1.43a4.563 4.563 0 
01-.543-.183c.122.048-.044-.02-.078-.035a4.77 4.77 0 01-.422-.212c-.594-.338-.955-.722-.872-1.369.105-.816.757-1.221 1.555-1.28.808-.06 1.648.135 
2.297.554.614.398 1.19-.553.58-.947-1.33-.86-3.504-1.074-4.77-.005z" clip-rule="evenodd"></path></svg>Shopee coins 
redeemable</div></div></div><section class="RqMReY" role="list"><div class="_9G37m"><div class="wsVAKH"><span class="lKqYHD">Bundle</span><span>Any 
2 for RM72.00</span><span class="Vm8iNU"><a href="/bundle-deal/221684290?from=cart">Add more<svg viewBox="0 0 12 12" fill="none" width="12" 
height="12" color="#ee4d2d" class="MuMxsb"><path fill-rule="evenodd" clip-rule="evenodd" d="M9.293 6L4.146.854l.708-.708L10 5.293a1 1 0 010 
1.414l-5.146 5.147-.708-.707L9.293 6z" fill="currentColor"></path></svg></a></span></div><div class="lDiGJB kEMRam" role="listitem"><h4 
class="a11y-hidden">cart_accessibility_item</h4><div class="f1bSN6"><div class="Xp4RLg"><label class="stardust-checkbox"><input 
class="stardust-checkbox__input" type="checkbox" aria-checked="false" aria-disabled="false" tabindex="0" role="checkbox" aria-label="Click here to 
select this product"><div class="stardust-checkbox__box"></div></label></div><div class="brf29Y"><div class="bzhajK"><a title="[UUCORNER] PREMIUM 
QUALITY W all in one seamless wireless jelly stick latex bra 无痕乳胶果冻内衣 baju dalam wanita" 
href="/-UUCORNER-PREMIUM-QUALITY-W-all-in-one-seamless-wireless-jelly-stick-latex-bra-无痕乳胶果冻内衣-baju-dalam-wanita-i.619427971.17063557923?xptdk
=c9c872b1-5f20-4cee-82bb-33e43e30b506"><img class="jFEiVQ" src="https://down-my.img.susercontent.com/file/dc784881c206dea75ec2da823e266542" 
alt="product image"></a><div class="Ou_0WX"><a class="c54pg1" title="[UUCORNER] PREMIUM QUALITY W all in one seamless wireless jelly stick latex 
bra 无痕乳胶果冻内衣 baju dalam wanita" href="/-UUCORNER-PREMIUM-QUALITY-W-all-in-one-seamless-wireless-jelly-stick-latex-bra-无痕乳胶果冻内衣-baju-dalam-wanita-i
.619427971.17063557923?xptdk=c9c872b1-5f20-4cee-82bb-33e43e30b506">[UUCORNER] PREMIUM QUALITY W all in one seamless wireless jelly stick latex bra 
无痕乳胶果冻内衣 baju dalam wanita</a><img class="Kv1AvK" src="https://down-my.img.susercontent.com/file/my-50009109-07d26479b71d36d840c404c716d03602"><div 
class="gvFc9h"></div></div></div><div class="Jkd76v bzhajK">RM 37.90 on 25 Feb Only</div></div><div class="eHDC_o"><div class="qNRZqG"><button 
class="mM4TZ8" role="button" tabindex="0"><div class="iIg1CN">Variations:<div class="E33rwr"></div></div><div class="dDPSp3">Silver grey,
S(32/70)</div></button><div></div></div></div><div class="gJyWia"><div><span class="vjkBXu">RM37.90</span></div></div><div class="sluy3i"><div 
class="GpmJtT shopee-input-quantity"><button class="WNSVcC" aria-label="Decrease"><svg enable-background="new 0 0 10 10" viewBox="0 0 10 10" x="0" 
y="0" class="shopee-svg-icon"><polygon points="4.5 4.5 3.5 4.5 0 4.5 0 5.5 3.5 5.5 4.5 5.5 10 5.5 10 4.5"></polygon></svg></button><input 
class="WNSVcC g2m9n4" type="text" role="spinbutton" aria-valuenow="1" value="1"><button class="WNSVcC" aria-label="Increase"><svg 
enable-background="new 0 0 10 10" viewBox="0 0 10 10" x="0" y="0" class="shopee-svg-icon icon-plus-sign"><polygon points="10 4.5 5.5 4.5 5.5 0 4.5 
0 4.5 4.5 0 4.5 0 5.5 4.5 5.5 4.5 10 5.5 10 5.5 5.5 10 5.5"></polygon></svg></button></div></div><div class="HRvCAv"><span>RM37.90</span><span 
class="a11y-hidden">Total price: RM37.90</span></div><div class="bRSn43 TvSDdG"><button class="lSrQtj">Delete</button><div class="J8cCGR"><button 
class="shopee-button-no-outline slfWNx"><span class="wZrjgF">Find Similar</span><svg enable-background="new 0 0 15 15" viewBox="0 0 15 15" x="0" 
y="0" class="shopee-svg-icon f3N1Rf icon-down-arrow-filled"><path d="m6.5 12.9-6-7.9s-1.4-1.5.5-1.5h13s1.8 0 .6 1.5l-6 7.9c-.1 0-.9 1.3-2.1 
0z"></path></svg></button></div></div></div></div><div class="t89ViJ"></div></div></section><div class="ArX7yj"><svg fill="none" viewBox="0 -2 23 
22" class="shopee-svg-icon lGPe96 icon-voucher-line"><g filter="url(#voucher-filter0_d)"><mask id="a" fill="#fff"><path fill-rule="evenodd" 
clip-rule="evenodd" d="M1 2h18v2.32a1.5 1.5 0 000 2.75v.65a1.5 1.5 0 000 2.75v.65a1.5 1.5 0 000 2.75V16H1v-2.12a1.5 1.5 0 000-2.75v-.65a1.5 1.5 0 
000-2.75v-.65a1.5 1.5 0 000-2.75V2z"></path></mask><path d="M19 2h1V1h-1v1zM1 2V1H0v1h1zm18 2.32l.4.92.6-.26v-.66h-1zm0 
2.75h1v-.65l-.6-.26-.4.91zm0 .65l.4.92.6-.26v-.66h-1zm0 2.75h1v-.65l-.6-.26-.4.91zm0 .65l.4.92.6-.26v-.66h-1zm0 2.75h1v-.65l-.6-.26-.4.91zM19 
16v1h1v-1h-1zM1 16H0v1h1v-1zm0-2.12l-.4-.92-.6.26v.66h1zm0-2.75H0v.65l.6.26.4-.91zm0-.65l-.4-.92-.6.26v.66h1zm0-2.75H0v.65l.6.26.4-.91zm0-.65l-.4
-.92-.6.26v.66h1zm0-2.75H0v.65l.6.26.4-.91zM19 1H1v2h18V1zm1 3.32V2h-2v2.32h2zm-.9 1.38c0-.2.12-.38.3-.46l-.8-1.83a2.5 2.5 0 00-1.5 
2.29h2zm.3.46a.5.5 0 01-.3-.46h-2c0 1.03.62 1.9 1.5 2.3l.8-1.84zm.6 1.56v-.65h-2v.65h2zm-.9 1.38c0-.2.12-.38.3-.46l-.8-1.83a2.5 2.5 0 00-1.5 
2.29h2zm.3.46a.5.5 0 01-.3-.46h-2c0 1.03.62 1.9 1.5 2.3l.8-1.84zm.6 1.56v-.65h-2v.65h2zm-.9 1.38c0-.2.12-.38.3-.46l-.8-1.83a2.5 2.5 0 00-1.5 
2.29h2zm.3.46a.5.5 0 01-.3-.46h-2c0 1.03.62 1.9 1.5 2.3l.8-1.84zM20 16v-2.13h-2V16h2zM1 17h18v-2H1v2zm-1-3.12V16h2v-2.12H0zm1.4.91a2.5 2.5 0 
001.5-2.29h-2a.5.5 0 01-.3.46l.8 1.83zm1.5-2.29a2.5 2.5 0 00-1.5-2.3l-.8 1.84c.18.08.3.26.3.46h2zM0 10.48v.65h2v-.65H0zM.9 9.1a.5.5 0 01-.3.46l.8 
1.83A2.5 2.5 0 002.9 9.1h-2zm-.3-.46c.18.08.3.26.3.46h2a2.5 2.5 0 00-1.5-2.3L.6 8.65zM0 7.08v.65h2v-.65H0zM.9 5.7a.5.5 0 01-.3.46l.8 1.83A2.5 2.5 0 
002.9 5.7h-2zm-.3-.46c.18.08.3.26.3.46h2a2.5 2.5 0 00-1.5-2.3L.6 5.25zM0 2v2.33h2V2H0z" mask="url(#a)"></path></g><path clip-rule="evenodd" 
d="M6.49 14.18h.86v-1.6h-.86v1.6zM6.49 11.18h.86v-1.6h-.86v1.6zM6.49 8.18h.86v-1.6h-.86v1.6zM6.49 5.18h.86v-1.6h-.86v1.6z"></path><defs><filter 
id="voucher-filter0_d" x="0" y="1" width="20" height="16" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB"><feFlood 
flood-opacity="0" result="BackgroundImageFix"></feFlood><feColorMatrix in="SourceAlpha" values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 127 
0"></feColorMatrix><feOffset></feOffset><feGaussianBlur stdDeviation=".5"></feGaussianBlur><feColorMatrix values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
0 0.09 0"></feColorMatrix><feBlend in2="BackgroundImageFix" result="effect1_dropShadow"></feBlend><feBlend in="SourceGraphic" 
in2="effect1_dropShadow" result="shape"></feBlend></filter></defs></svg><div class="N9nCmB"><div class="nKTIzW">Up to RM5 off voucher 
available</div><div class="JC72Dv"><button class="qe2YoR">More Vouchers</button><div style="display: contents;"></div></div></div></div><div 
class="_RPX38"><img width="20" height="20" src="https://deo.shopeemobile.com/shopee/shopee-pcmall-live-sg/cart/094f639ce7dff28ced5b.png" 
alt="fs-icon"><div class="Cmb29y">Up to RM5.00 off shipping for orders over RM0.00</div><div class="shopee-drawer" id="pc-drawer-id-10" 
tabindex="0"><span class="Eb1Wor" aria-describedby="619427971_shipping_discount"> Learn more </span></div></div></section><section 
class="AuhAvM"><h3 class="a11y-hidden">Shop Section</h3><div class="JsC6Oq NWPcV8"><div class="gzSvrb"><div class="Ll5dDW"><label 
class="stardust-checkbox"><input class="stardust-checkbox__input" type="checkbox" aria-checked="false" tabindex="0" role="checkbox" 
aria-label="Click here to select all products in Seven Street"><div class="stardust-checkbox__box"></div></label></div><a class="QcqMX5" 
href="/sevenstreet.os?categoryId=100017&amp;entryPoint=cart&amp;itemId=4261183275"><div><svg width="17" height="16" viewBox="0 0 17 16" 
class="Koi0Pw"><title>Shop Icon</title><path d="M1.95 6.6c.156.804.7 1.867 1.357 1.867.654 0 1.43 0 1.43-.933h.932s0 .933 1.155.933c1.176 0 
1.15-.933 1.15-.933h.984s-.027.933 1.148.933c1.157 0 1.15-.933 1.15-.933h.94s0 .933 1.43.933c1.368 0 1.356-1.867 
1.356-1.867H1.95zm11.49-4.666H3.493L2.248 5.667h12.437L13.44 1.934zM2.853 14.066h11.22l-.01-4.782c-.148.02-.295.042-.465.042-.7 
0-1.436-.324-1.866-.86-.376.53-.88.86-1.622.86-.667 0-1.255-.417-1.64-.86-.39.443-.976.86-1.643.86-.74 
0-1.246-.33-1.623-.86-.43.536-1.195.86-1.895.86-.152 0-.297-.02-.436-.05l-.018 4.79zM14.996 12.2v.933L14.984 15H1.94l-.002-1.867V8.84C1.355 8.306 
1.003 7.456 1 6.6L2.87 1h11.193l1.866 5.6c0 .943-.225 1.876-.934 2.39v3.21z" stroke-width=".3" stroke="#333" fill="#333" 
fill-rule="evenodd"></path></svg></div><span style="margin-left: 10px;">Seven Street</span></a><button class="Eg4UEE"><svg viewBox="0 0 16 16" 
class="shopee-svg-icon AxeMgG"><g fill-rule="evenodd"><path d="M15 4a1 1 0 01.993.883L16 5v9.932a.5.5 0 01-.82.385l-2.061-1.718-8.199.001a1 1 0 
01-.98-.8l-.016-.117-.108-1.284 8.058.001a2 2 0 001.976-1.692l.018-.155L14.293 4H15zm-2.48-4a1 1 0 011 1l-.003.077-.646 8.4a1 1 0 
01-.997.923l-8.994-.001-2.06 1.718a.5.5 0 01-.233.108l-.087.007a.5.5 0 01-.492-.41L0 11.732V1a1 1 0 011-1h11.52zM3.646 4.246a.5.5 0 000 
.708c.305.304.694.526 1.146.682A4.936 4.936 0 006.4 5.9c.464 0 1.02-.062 1.608-.264.452-.156.841-.378 1.146-.682a.5.5 0 
10-.708-.708c-.185.186-.445.335-.764.444a4.004 4.004 0 01-2.564 0c-.319-.11-.579-.258-.764-.444a.5.5 0 00-.708 0z"></path></g></svg></button><div 
class="cVlPY7"></div></div></div><section class="RqMReY" role="list"><div class="_9G37m"><div class="wsVAKH"><span class="lKqYHD">Free 
Gift</span><span>Spend RM35.00 to get 1 free gift</span><span class="Vm8iNU"><a 
href="/purchase-with-gifts/135769083936790/4261183275/53648977?showGifts=0">Add more<svg viewBox="0 0 12 12" fill="none" width="12" height="12" 
color="#ee4d2d" class="MuMxsb"><path fill-rule="evenodd" clip-rule="evenodd" d="M9.293 6L4.146.854l.708-.708L10 5.293a1 1 0 010 1.414l-5.146 
5.147-.708-.707L9.293 6z" fill="currentColor"></path></svg></a></span></div><div class="lDiGJB kEMRam" role="listitem"><h4 
class="a11y-hidden">cart_accessibility_item</h4><div class="f1bSN6"><div class="Xp4RLg"><label class="stardust-checkbox"><input 
class="stardust-checkbox__input" type="checkbox" aria-checked="false" aria-disabled="false" tabindex="0" role="checkbox" aria-label="Click here to 
select this product"><div class="stardust-checkbox__box"></div></label></div><div class="brf29Y"><div class="bzhajK"><a title="Seven Street 1 box 4 
pcs Woman Anti-bacterial Mid Waist Cotton Panties Underwear Seluar Dalam Wanita" 
href="/Seven-Street-1-box-4-pcs-Woman-Anti-bacterial-Mid-Waist-Cotton-Panties-Underwear-Seluar-Dalam-Wanita-i.53648977.4261183275?xptdk=5123d8cc
-4d72-47b7-bc1a-d4dd2a0359e7"><img class="jFEiVQ" src="https://down-my.img.susercontent.com/file/5cdc2042de398079c29186886fe54e75" alt="product 
image"></a><div class="Ou_0WX"><a class="c54pg1" title="Seven Street 1 box 4 pcs Woman Anti-bacterial Mid Waist Cotton Panties Underwear Seluar 
Dalam Wanita" href="/Seven-Street-1-box-4-pcs-Woman-Anti-bacterial-Mid-Waist-Cotton-Panties-Underwear-Seluar-Dalam-Wanita-i.53648977.4261183275
?xptdk=5123d8cc-4d72-47b7-bc1a-d4dd2a0359e7">Seven Street 1 box 4 pcs Woman Anti-bacterial Mid Waist Cotton Panties Underwear Seluar Dalam 
Wanita</a><img class="Kv1AvK" src="https://down-my.img.susercontent.com/file/my-50009109-07d26479b71d36d840c404c716d03602"><div 
class="gvFc9h"></div></div></div><div class="Jkd76v bzhajK">RM 14.50 on 25 Feb Only</div></div><div class="eHDC_o"><div class="qNRZqG 
IlkVEv"><button class="mM4TZ8" role="button" tabindex="0" disabled=""><div class="iIg1CN">Variations:</div><div class="dDPSp3">4pcs per 
box</div></button><div></div></div></div><div class="gJyWia"><div><span class="vjkBXu tnTSPU">RM15.90</span><span 
class="vjkBXu">RM14.50</span></div></div><div class="sluy3i"><div class="GpmJtT shopee-input-quantity"><button class="WNSVcC" 
aria-label="Decrease"><svg enable-background="new 0 0 10 10" viewBox="0 0 10 10" x="0" y="0" class="shopee-svg-icon"><polygon points="4.5 4.5 3.5 
4.5 0 4.5 0 5.5 3.5 5.5 4.5 5.5 10 5.5 10 4.5"></polygon></svg></button><input class="WNSVcC g2m9n4" type="text" role="spinbutton" 
aria-valuenow="1" value="1"><button class="WNSVcC" aria-label="Increase"><svg enable-background="new 0 0 10 10" viewBox="0 0 10 10" x="0" y="0" 
class="shopee-svg-icon icon-plus-sign"><polygon points="10 4.5 5.5 4.5 5.5 0 4.5 0 4.5 4.5 0 4.5 0 5.5 4.5 5.5 4.5 10 5.5 10 5.5 5.5 10 
5.5"></polygon></svg></button></div></div><div class="HRvCAv"><span>RM14.50</span><span class="a11y-hidden">Total price: RM14.50</span></div><div 
class="bRSn43 TvSDdG"><button class="lSrQtj">Delete</button><div class="J8cCGR"><button class="shopee-button-no-outline slfWNx"><span 
class="wZrjgF">Find Similar</span><svg enable-background="new 0 0 15 15" viewBox="0 0 15 15" x="0" y="0" class="shopee-svg-icon f3N1Rf 
icon-down-arrow-filled"><path d="m6.5 12.9-6-7.9s-1.4-1.5.5-1.5h13s1.8 0 .6 1.5l-6 7.9c-.1 0-.9 1.3-2.1 
0z"></path></svg></button></div></div></div></div><div class="t89ViJ"></div></div></section><div class="ArX7yj"><svg fill="none" viewBox="0 -2 23 
22" class="shopee-svg-icon lGPe96 icon-voucher-line"><g filter="url(#voucher-filter0_d)"><mask id="a" fill="#fff"><path fill-rule="evenodd" 
clip-rule="evenodd" d="M1 2h18v2.32a1.5 1.5 0 000 2.75v.65a1.5 1.5 0 000 2.75v.65a1.5 1.5 0 000 2.75V16H1v-2.12a1.5 1.5 0 000-2.75v-.65a1.5 1.5 0 
000-2.75v-.65a1.5 1.5 0 000-2.75V2z"></path></mask><path d="M19 2h1V1h-1v1zM1 2V1H0v1h1zm18 2.32l.4.92.6-.26v-.66h-1zm0 
2.75h1v-.65l-.6-.26-.4.91zm0 .65l.4.92.6-.26v-.66h-1zm0 2.75h1v-.65l-.6-.26-.4.91zm0 .65l.4.92.6-.26v-.66h-1zm0 2.75h1v-.65l-.6-.26-.4.91zM19 
16v1h1v-1h-1zM1 16H0v1h1v-1zm0-2.12l-.4-.92-.6.26v.66h1zm0-2.75H0v.65l.6.26.4-.91zm0-.65l-.4-.92-.6.26v.66h1zm0-2.75H0v.65l.6.26.4-.91zm0-.65l-.4
-.92-.6.26v.66h1zm0-2.75H0v.65l.6.26.4-.91zM19 1H1v2h18V1zm1 3.32V2h-2v2.32h2zm-.9 1.38c0-.2.12-.38.3-.46l-.8-1.83a2.5 2.5 0 00-1.5 
2.29h2zm.3.46a.5.5 0 01-.3-.46h-2c0 1.03.62 1.9 1.5 2.3l.8-1.84zm.6 1.56v-.65h-2v.65h2zm-.9 1.38c0-.2.12-.38.3-.46l-.8-1.83a2.5 2.5 0 00-1.5 
2.29h2zm.3.46a.5.5 0 01-.3-.46h-2c0 1.03.62 1.9 1.5 2.3l.8-1.84zm.6 1.56v-.65h-2v.65h2zm-.9 1.38c0-.2.12-.38.3-.46l-.8-1.83a2.5 2.5 0 00-1.5 
2.29h2zm.3.46a.5.5 0 01-.3-.46h-2c0 1.03.62 1.9 1.5 2.3l.8-1.84zM20 16v-2.13h-2V16h2zM1 17h18v-2H1v2zm-1-3.12V16h2v-2.12H0zm1.4.91a2.5 2.5 0 
001.5-2.29h-2a.5.5 0 01-.3.46l.8 1.83zm1.5-2.29a2.5 2.5 0 00-1.5-2.3l-.8 1.84c.18.08.3.26.3.46h2zM0 10.48v.65h2v-.65H0zM.9 9.1a.5.5 0 01-.3.46l.8 
1.83A2.5 2.5 0 002.9 9.1h-2zm-.3-.46c.18.08.3.26.3.46h2a2.5 2.5 0 00-1.5-2.3L.6 8.65zM0 7.08v.65h2v-.65H0zM.9 5.7a.5.5 0 01-.3.46l.8 1.83A2.5 2.5 0 
002.9 5.7h-2zm-.3-.46c.18.08.3.26.3.46h2a2.5 2.5 0 00-1.5-2.3L.6 5.25zM0 2v2.33h2V2H0z" mask="url(#a)"></path></g><path clip-rule="evenodd" 
d="M6.49 14.18h.86v-1.6h-.86v1.6zM6.49 11.18h.86v-1.6h-.86v1.6zM6.49 8.18h.86v-1.6h-.86v1.6zM6.49 5.18h.86v-1.6h-.86v1.6z"></path><defs><filter 
id="voucher-filter0_d" x="0" y="1" width="20" height="16" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB"><feFlood 
flood-opacity="0" result="BackgroundImageFix"></feFlood><feColorMatrix in="SourceAlpha" values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 127 
0"></feColorMatrix><feOffset></feOffset><feGaussianBlur stdDeviation=".5"></feGaussianBlur><feColorMatrix values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
0 0.09 0"></feColorMatrix><feBlend in2="BackgroundImageFix" result="effect1_dropShadow"></feBlend><feBlend in="SourceGraphic" 
in2="effect1_dropShadow" result="shape"></feBlend></filter></defs></svg><div class="N9nCmB"><div class="nKTIzW">Up to 99% off voucher 
available</div><div class="JC72Dv"><button class="qe2YoR">More Vouchers</button><div style="display: contents;"></div></div></div></div><div 
class="_RPX38"><img width="20" height="20" src="https://deo.shopeemobile.com/shopee/shopee-pcmall-live-sg/cart/094f639ce7dff28ced5b.png" 
alt="fs-icon"><div class="Cmb29y">Up to RM5.00 off shipping for orders over RM0.00</div><div class="shopee-drawer" id="pc-drawer-id-11" 
tabindex="0"><span class="Eb1Wor" aria-describedby="53648977_shipping_discount"> Learn more </span></div></div></section><div class="i0KH4X"><div 
class="IKhPFB"><div class="d_Ml8J"><label class="stardust-checkbox stardust-checkbox--disabled"><input class="stardust-checkbox__input" 
type="checkbox" aria-checked="false" aria-disabled="true" tabindex="0" role="checkbox"><div class="stardust-checkbox__box"></div></label></div><div 
class="Xe6VCd Ljj5Rm"></div></div><div class="Q5AWdP"><div class="d_Ml8J"><label class="stardust-checkbox stardust-checkbox--disabled"><input 
class="stardust-checkbox__input" type="checkbox" aria-checked="false" aria-disabled="true" tabindex="0" role="checkbox"><div 
class="stardust-checkbox__box"></div></label></div><div class="MV29in"><div class="YeMuYt"></div></div><div class="eupcUt"><div class="Xe6VCd 
Ljj5Rm"></div><div class="Xe6VCd Ljj5Rm"></div></div></div><div class="QSKD5J"></div><div class="Q5AWdP"><div class="d_Ml8J"><label 
class="stardust-checkbox stardust-checkbox--disabled"><input class="stardust-checkbox__input" type="checkbox" aria-checked="false" 
aria-disabled="true" tabindex="0" role="checkbox"><div class="stardust-checkbox__box"></div></label></div><div class="MV29in"><div 
class="YeMuYt"></div></div><div class="eupcUt"><div class="Xe6VCd zgsXzo"></div><div class="Xe6VCd zgsXzo"></div></div></div><div 
class="QSKD5J"></div><div class="Q5AWdP"><div class="d_Ml8J"><label class="stardust-checkbox stardust-checkbox--disabled"><input 
class="stardust-checkbox__input" type="checkbox" aria-checked="false" aria-disabled="true" tabindex="0" role="checkbox"><div 
class="stardust-checkbox__box"></div></label></div><div class="MV29in"><div class="YeMuYt"></div></div><div class="eupcUt"><div class="Xe6VCd 
TFHK02"></div><div class="Xe6VCd TFHK02"></div></div></div><div class="SP3KGO"><div class="Xe6VCd Ljj5Rm"></div></div><div class="SP3KGO"><div 
class="Xe6VCd Ljj5Rm"></div></div></div></main><section class="yn6AIc dhqg2H"><h2 class="a11y-hidden">cart_accessibility_footer</h2><div 
class="CzLyKQ lRHCcS"><h3 class="a11y-hidden">cart_accessibility_footer_voucher_row</h3><svg fill="none" viewBox="0 -2 23 22" 
class="shopee-svg-icon icon-voucher-line"><g filter="url(#voucher-filter0_d)"><mask id="a" fill="#fff"><path fill-rule="evenodd" 
clip-rule="evenodd" d="M1 2h18v2.32a1.5 1.5 0 000 2.75v.65a1.5 1.5 0 000 2.75v.65a1.5 1.5 0 000 2.75V16H1v-2.12a1.5 1.5 0 000-2.75v-.65a1.5 1.5 0 
000-2.75v-.65a1.5 1.5 0 000-2.75V2z"></path></mask><path d="M19 2h1V1h-1v1zM1 2V1H0v1h1zm18 2.32l.4.92.6-.26v-.66h-1zm0 
2.75h1v-.65l-.6-.26-.4.91zm0 .65l.4.92.6-.26v-.66h-1zm0 2.75h1v-.65l-.6-.26-.4.91zm0 .65l.4.92.6-.26v-.66h-1zm0 2.75h1v-.65l-.6-.26-.4.91zM19 
16v1h1v-1h-1zM1 16H0v1h1v-1zm0-2.12l-.4-.92-.6.26v.66h1zm0-2.75H0v.65l.6.26.4-.91zm0-.65l-.4-.92-.6.26v.66h1zm0-2.75H0v.65l.6.26.4-.91zm0-.65l-.4
-.92-.6.26v.66h1zm0-2.75H0v.65l.6.26.4-.91zM19 1H1v2h18V1zm1 3.32V2h-2v2.32h2zm-.9 1.38c0-.2.12-.38.3-.46l-.8-1.83a2.5 2.5 0 00-1.5 
2.29h2zm.3.46a.5.5 0 01-.3-.46h-2c0 1.03.62 1.9 1.5 2.3l.8-1.84zm.6 1.56v-.65h-2v.65h2zm-.9 1.38c0-.2.12-.38.3-.46l-.8-1.83a2.5 2.5 0 00-1.5 
2.29h2zm.3.46a.5.5 0 01-.3-.46h-2c0 1.03.62 1.9 1.5 2.3l.8-1.84zm.6 1.56v-.65h-2v.65h2zm-.9 1.38c0-.2.12-.38.3-.46l-.8-1.83a2.5 2.5 0 00-1.5 
2.29h2zm.3.46a.5.5 0 01-.3-.46h-2c0 1.03.62 1.9 1.5 2.3l.8-1.84zM20 16v-2.13h-2V16h2zM1 17h18v-2H1v2zm-1-3.12V16h2v-2.12H0zm1.4.91a2.5 2.5 0 
001.5-2.29h-2a.5.5 0 01-.3.46l.8 1.83zm1.5-2.29a2.5 2.5 0 00-1.5-2.3l-.8 1.84c.18.08.3.26.3.46h2zM0 10.48v.65h2v-.65H0zM.9 9.1a.5.5 0 01-.3.46l.8 
1.83A2.5 2.5 0 002.9 9.1h-2zm-.3-.46c.18.08.3.26.3.46h2a2.5 2.5 0 00-1.5-2.3L.6 8.65zM0 7.08v.65h2v-.65H0zM.9 5.7a.5.5 0 01-.3.46l.8 1.83A2.5 2.5 0 
002.9 5.7h-2zm-.3-.46c.18.08.3.26.3.46h2a2.5 2.5 0 00-1.5-2.3L.6 5.25zM0 2v2.33h2V2H0z" mask="url(#a)"></path></g><path clip-rule="evenodd" 
d="M6.49 14.18h.86v-1.6h-.86v1.6zM6.49 11.18h.86v-1.6h-.86v1.6zM6.49 8.18h.86v-1.6h-.86v1.6zM6.49 5.18h.86v-1.6h-.86v1.6z"></path><defs><filter 
id="voucher-filter0_d" x="0" y="1" width="20" height="16" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB"><feFlood 
flood-opacity="0" result="BackgroundImageFix"></feFlood><feColorMatrix in="SourceAlpha" values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 127 
0"></feColorMatrix><feOffset></feOffset><feGaussianBlur stdDeviation=".5"></feGaussianBlur><feColorMatrix values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
0 0.09 0"></feColorMatrix><feBlend in2="BackgroundImageFix" result="effect1_dropShadow"></feBlend><feBlend in="SourceGraphic" 
in2="effect1_dropShadow" result="shape"></feBlend></filter></defs></svg><div class="FGs2jP">Platform Voucher</div><div class="oI3JPG"></div><button 
class="nOoMrG">Select or enter code</button></div><div class="Z6oxZ3 iDgxib"></div><h3 
class="a11y-hidden">cart_accessibility_footer_coin_row</h3><div class="WuLbM9 BjTxuU"><label class="stardust-checkbox 
stardust-checkbox--disabled"><input class="stardust-checkbox__input" type="checkbox" aria-checked="false" aria-disabled="true" tabindex="0" 
role="checkbox" aria-label="Coins Balance 0"><div class="stardust-checkbox__box"></div></label></div><div class="WuLbM9 ificCM dOZlXw T5n8VV"><svg 
fill="none" viewBox="0 0 18 18" class="shopee-svg-icon Iz070x icon-coin-line"><path stroke="#FFA600" stroke-width="1.3" d="M17.35 9A8.35 8.35 0 
11.65 9a8.35 8.35 0 0116.7 0z"></path><path fill="#FFA600" fill-rule="evenodd" stroke="#FFA600" stroke-width=".2" d="M6.86 4.723c-.683.576-.998 
1.627-.75 2.464.215.725.85 1.258 1.522 1.608.37.193.77.355 
1.177.463.1.027.2.051.3.08.098.03.196.062.294.096.06.021.121.044.182.067.017.006.107.041.04.014-.07-.028.071.03.087.037.286.124.56.27.82.44.114.076
.045.024.151.111a2.942 2.942 0 01.322.303c.087.093.046.042.114.146.18.275.245.478.235.8-.01.328-.14.659-.325.867-.47.53-1.232.73-1.934.696a4.727 
4.727 0 01-1.487-.307c-.45-.182-.852-.462-1.242-.737-.25-.176-.643-.04-.788.197-.17.279-.044.574.207.75.753.532 1.539.946 2.474 1.098.885.144 
1.731.124 2.563-.224.78-.326 1.416-.966 1.607-1.772.198-.838-.023-1.644-.61-2.29-.683-.753-1.722-1.17-2.706-1.43a4.563 4.563 0 
01-.543-.183c.122.048-.044-.02-.078-.035a4.77 4.77 0 01-.422-.212c-.594-.338-.955-.722-.872-1.369.105-.816.757-1.221 1.555-1.28.808-.06 1.648.135 
2.297.554.614.398 1.19-.553.58-.947-1.33-.86-3.504-1.074-4.77-.005z" clip-rule="evenodd"></path></svg><div class="BBQR6_">Shopee Coins</div><div 
class="PkMsif">No item selected</div><div class="stardust-popover Prdzh0" id="stardust-popover0" tabindex="0"><div role="button" 
class="stardust-popover__target"><div><svg enable-background="new 0 0 15 15" viewBox="0 0 15 15" x="0" y="0" class="shopee-svg-icon eXBxkv 
icon-help"><g><circle cx="7.5" cy="7.5" fill="none" r="6.5" stroke-miterlimit="10"></circle><path d="m5.3 5.3c.1-.3.3-.6.5-.8s.4-.4.7-.5.6-.2 
1-.2c.3 0 .6 0 .9.1s.5.2.7.4.4.4.5.7.2.6.2.9c0 .2 0 .4-.1.6s-.1.3-.2.5c-.1.1-.2.2-.3.3-.1.2-.2.3-.4.4-.1.1-.2.2-.3.3s-.2.2-.3.4c-.1.1-.1.2-.2.4s-.1
.3-.1.5v.4h-.9v-.5c0-.3.1-.6.2-.8s.2-.4.3-.5c.2-.2.3-.3.5-.5.1-.1.3-.3.4-.4.1-.2.2-.3.3-.5s.1-.4.1-.7c0-.4-.2-.7-.4-.9s-.5-.3-.9-.3c-.3 0-.5 
0-.7.1-.1.1-.3.2-.4.4-.1.1-.2.3-.3.5 0 .2-.1.5-.1.7h-.9c0-.3.1-.7.2-1zm2.8 5.1v1.2h-1.2v-1.2z" 
stroke="none"></path></g></svg></div></div></div></div><div class="WuLbM9 fDdBqs IR54W9">-RM0.00</div><div class="Z6oxZ3 MOZmZ1"></div><div 
class="WhvsrO Kk1Mak"><h3 class="a11y-hidden">cart_accessibility_footer_checkout_row</h3><div class="u4pma8"><label 
class="stardust-checkbox"><input class="stardust-checkbox__input" type="checkbox" aria-checked="false" aria-disabled="false" tabindex="0" 
role="checkbox" aria-label="Click here to select all products"><div class="stardust-checkbox__box"></div></label></div><button class="v5CBXg 
clear-btn-style">Select All (15)</button><button class="clear-btn-style GQ7Hga">Delete</button><div class=""></div><button class="clear-btn-style 
QmkEaL">Move to My Likes</button><div class="iqpIui"></div><div class="BV92a3" role="region"><div class="DScaTh"><div class="znJ7TE"><div 
class="CoYXUV">Total (0 item):</div><div class="mketV9">RM0.00</div></div></div><div class="unV7eM"></div></div><button class="shopee-button-solid 
shopee-button-solid--primary"><span class="SHq91i">check out</span></button></div></section></div><div><div style="height: 
1px;"></div></div></div></div><footer role="contentinfo" class="_5mVtqL uZncG4"><div class="PjIOU+"><div><div style="height: 
1px;"></div></div></div></footer></div><div></div><div class="u+rzIW" id="BackgroundImagePortalAnchor"></div></div></div>
</noscript>
<div id="modal"><div><div class="shopee-modal__transition-appear-done shopee-modal__transition-enter-done"></div></div><div><div 
class="shopee-modal__transition-appear-done shopee-modal__transition-enter-done"></div></div></div>
<script type="module" src="https://deo.shopeemobile.com/shopee/shopee-pcmall-live-sg/assets/webpack-runtime.aded303e8cdc77bb.js"></script>
<script type="module" src="https://deo.shopeemobile.com/shopee/shopee-pcmall-live-sg/assets/7008.6b2a9aafa20b6b03.js"></script>
<script type="module" src="https://deo.shopeemobile.com/shopee/shopee-pcmall-live-sg/assets/bundle.4be69fbdf1aba551.js"></script>
<script nomodule="">function loadStyleLink(e){var l=document.head||document.getElementsByTagName("head")[0],t=document.createElement(
"link");t.rel="stylesheet",t.type="text/css",t.href=e,l.appendChild(t)}if(!SUPPORT_MODULE){for(var links=[
"https://deo.shopeemobile.com/shopee/shopee-pcmall-live-sg/assets/350.e267fe02bfcc4d14.legacy.css",
"https://deo.shopeemobile.com/shopee/shopee-pcmall-live-sg/assets/bundle.ef2f5a50e18ada28.legacy.css"],i=0;i<links.length;i++)loadStyleLink(links[
i]);try{document.querySelectorAll("[data-modern]").forEach((function(e){e.parentNode.removeChild(e)}))}catch(e){}}</script><script 
src="https://deo.shopeemobile.com/shopee/shopee-pcmall-live-sg/assets/webpack-runtime.43512701549f1fa5.legacy.js" defer="defer" 
nomodule=""></script><script src="https://deo.shopeemobile.com/shopee/shopee-pcmall-live-sg/assets/350.df53f5ad7c76e367.legacy.js" defer="defer" 
nomodule=""></script><script src="https://deo.shopeemobile.com/shopee/shopee-pcmall-live-sg/assets/bundle.d44bce1390ca7082.legacy.js" defer="defer" 
nomodule=""></script>

<script async="" src="https://deo.shopeemobile.com/shopee/shopee-trackingsdk-live-sg/@shopee/tracking-loader@1.1.20.min.js"></script><script 
async="" src="https://deo.shopeemobile.com/shopee/shopee-trackingsdk-live-sg/require-trackingsdk.js"></script><div class="stardust-toast__overlay" 
style="position: fixed; top: 0px; left: 0px; height: 100%; width: 100%; pointer-events: 
none;"><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div></div><script 
src="https://deo.shopeemobile.com/shopee/shopee-seller-live-my/chateasy/runtime.2c860350efef3ffb3555.js" type="module" charset="utf-8" 
crossorigin="anonymous" defer=""></script><script src="https://deo.shopeemobile.com/shopee/shopee-seller-live-my/chateasy/shopee-ui
.354ce3bc6447bf25fac8.js" type="module" charset="utf-8" crossorigin="anonymous" defer=""></script><script 
src="https://deo.shopeemobile.com/shopee/shopee-seller-live-my/chateasy/base2.fb642c30bef4541e8bdc.js" type="module" charset="utf-8" 
crossorigin="anonymous" defer=""></script><script src="https://deo.shopeemobile.com/shopee/shopee-seller-live-my/chateasy/safety
.7b31c8a42d6d864699aa.js" type="module" charset="utf-8" crossorigin="anonymous" defer=""></script><script 
src="https://deo.shopeemobile.com/shopee/shopee-seller-live-my/chateasy/mdap.5e09d98319ceff3d0ef1.js" type="module" charset="utf-8" 
crossorigin="anonymous" defer=""></script><script src="https://deo.shopeemobile.com/shopee/shopee-seller-live-my/chateasy/utils
.7d0d6501b0b2dd4f28a1.js" type="module" charset="utf-8" crossorigin="anonymous" defer=""></script><script 
src="https://deo.shopeemobile.com/shopee/shopee-seller-live-my/chateasy/self.8b41c776f340024dd407.js" type="module" charset="utf-8" 
crossorigin="anonymous" defer=""></script><script src="https://deo.shopeemobile.com/shopee/shopee-seller-live-my/chateasy/chat-ui
.0668c5a2e87d7778621d.js" type="module" charset="utf-8" crossorigin="anonymous" defer=""></script><script 
src="https://deo.shopeemobile.com/shopee/shopee-seller-live-my/chateasy/common.92eb5529e6c90a7e801e.js" type="module" charset="utf-8" 
crossorigin="anonymous" defer=""></script><script src="https://deo.shopeemobile.com/shopee/shopee-seller-live-my/chateasy/conversations
.a2a26e28582d5b9bc715.js" type="module" charset="utf-8" crossorigin="anonymous" defer=""></script><script 
src="https://deo.shopeemobile.com/shopee/shopee-seller-live-my/chateasy/vendors.cdd60c62.cd035ab67db05cce6099.js" type="module" charset="utf-8" 
crossorigin="anonymous" defer=""></script><script src="https://deo.shopeemobile.com/shopee/shopee-seller-live-my/chateasy/vendors.f82e0cd2
.31771e6a3fd4e491feeb.js" type="module" charset="utf-8" crossorigin="anonymous" defer=""></script><script 
src="https://deo.shopeemobile.com/shopee/shopee-seller-live-my/chateasy/vendors.866ab763.485541ddc59cbda12512.js" type="module" charset="utf-8" 
crossorigin="anonymous" defer=""></script><script src="https://deo.shopeemobile.com/shopee/shopee-seller-live-my/chateasy/5924.ac75d14a7dd1edb67538
.js" type="module" charset="utf-8" crossorigin="anonymous" defer=""></script><script 
src="https://deo.shopeemobile.com/shopee/shopee-seller-live-my/chateasy/app.3f78a4db3abf4f59a39e.js" type="module" charset="utf-8" 
crossorigin="anonymous" defer=""></script><link href="https://deo.shopeemobile.com/shopee/shopee-seller-live-my/chateasy/4312.8a1318ab1382dbcb216c
.css" rel="stylesheet" type="text/css" crossorigin="anonymous" data-chat-modern="true"><link 
href="https://deo.shopeemobile.com/shopee/shopee-seller-live-my/chateasy/app.28f9aaba735be564d93f.css" rel="stylesheet" type="text/css" 
crossorigin="anonymous" data-chat-modern="true"><script 
src="https://deo.shopeemobile.com/shopee/shopee-seller-live-my/chateasy/runtime.7041742526d4a60c45dc.js" type="text/javascript" charset="utf-8" 
crossorigin="anonymous" defer="" nomodule=""></script><script 
src="https://deo.shopeemobile.com/shopee/shopee-seller-live-my/chateasy/shopee-ui.354ce3bc6447bf25fac8.js" type="text/javascript" charset="utf-8" 
crossorigin="anonymous" defer="" nomodule=""></script><script 
src="https://deo.shopeemobile.com/shopee/shopee-seller-live-my/chateasy/base2.fb642c30bef4541e8bdc.js" type="text/javascript" charset="utf-8" 
crossorigin="anonymous" defer="" nomodule=""></script><script 
src="https://deo.shopeemobile.com/shopee/shopee-seller-live-my/chateasy/safety.7b31c8a42d6d864699aa.js" type="text/javascript" charset="utf-8" 
crossorigin="anonymous" defer="" nomodule=""></script><script 
src="https://deo.shopeemobile.com/shopee/shopee-seller-live-my/chateasy/mdap.6bf68be3b71ffa618a7d.js" type="text/javascript" charset="utf-8" 
crossorigin="anonymous" defer="" nomodule=""></script><script 
src="https://deo.shopeemobile.com/shopee/shopee-seller-live-my/chateasy/utils.65fd04cea39a98b184d3.js" type="text/javascript" charset="utf-8" 
crossorigin="anonymous" defer="" nomodule=""></script><script 
src="https://deo.shopeemobile.com/shopee/shopee-seller-live-my/chateasy/self.8b41c776f340024dd407.js" type="text/javascript" charset="utf-8" 
crossorigin="anonymous" defer="" nomodule=""></script><script 
src="https://deo.shopeemobile.com/shopee/shopee-seller-live-my/chateasy/chat-ui.72a4a9f2883bbea5c471.js" type="text/javascript" charset="utf-8" 
crossorigin="anonymous" defer="" nomodule=""></script><script 
src="https://deo.shopeemobile.com/shopee/shopee-seller-live-my/chateasy/common.3c16ac87b5fa65db323a.js" type="text/javascript" charset="utf-8" 
crossorigin="anonymous" defer="" nomodule=""></script><script 
src="https://deo.shopeemobile.com/shopee/shopee-seller-live-my/chateasy/conversations.ef10d0beacc94ea8352e.js" type="text/javascript" 
charset="utf-8" crossorigin="anonymous" defer="" nomodule=""></script><script 
src="https://deo.shopeemobile.com/shopee/shopee-seller-live-my/chateasy/vendors.cdd60c62.cd035ab67db05cce6099.js" type="text/javascript" 
charset="utf-8" crossorigin="anonymous" defer="" nomodule=""></script><script 
src="https://deo.shopeemobile.com/shopee/shopee-seller-live-my/chateasy/vendors.f82e0cd2.31771e6a3fd4e491feeb.js" type="text/javascript" 
charset="utf-8" crossorigin="anonymous" defer="" nomodule=""></script><script 
src="https://deo.shopeemobile.com/shopee/shopee-seller-live-my/chateasy/vendors.866ab763.485541ddc59cbda12512.js" type="text/javascript" 
charset="utf-8" crossorigin="anonymous" defer="" nomodule=""></script><script 
src="https://deo.shopeemobile.com/shopee/shopee-seller-live-my/chateasy/5924.9a1d86a64246b3278f8a.js" type="text/javascript" charset="utf-8" 
crossorigin="anonymous" defer="" nomodule=""></script><script 
src="https://deo.shopeemobile.com/shopee/shopee-seller-live-my/chateasy/app.3f78a4db3abf4f59a39e.js" type="text/javascript" charset="utf-8" 
crossorigin="anonymous" defer="" nomodule=""></script><script nomodule="">function loadStyleLink (links) {var head = document.head || 
document.getElementsByTagName("head")[0];for (var j = 0; j < links.length; j++) {var linkTag = document.createElement("link");linkTag.href = links[
j];linkTag.rel = "stylesheet";linkTag.type = "text/css";linkTag.crossOrigin = "anonymous";if (linkTag) {head.appendChild(linkTag);}}try {
document.querySelectorAll("[data-chat-modern]").forEach(function(e) {e.parentNode.removeChild(e)})} catch(e) {}}loadStyleLink([
'https://deo.shopeemobile.com/shopee/shopee-seller-live-my/chateasy/4312.8a1318ab1382dbcb216c.css',
'https://deo.shopeemobile.com/shopee/shopee-seller-live-my/chateasy/app.28f9aaba735be564d93f.css'])</script><div id="shopee-mini-chat-embedded" 
style="position: fixed; z-index: 99999; right: 8px; bottom: 0px;"><div class="
    bGX0VV9OFp
    VMBV0_VURc
    t9J4UYN3jm
  "><div class="r2v9ozyahe"><i class="GHUxSkxNuJ m3Mb2Tqdlw"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" class="chat-icon"><path 
  d="M18 6.07a1 1 0 01.993.883L19 7.07v10.365a1 1 0 01-1.64.768l-1.6-1.333H6.42a1 1 0 01-.98-.8l-.016-.117-.149-1.783h9.292a1.8 1.8 0 
  001.776-1.508l.018-.154.494-6.438H18zm-2.78-4.5a1 1 0 011 1l-.003.077-.746 9.7a1 1 0 01-.997.923H4.24l-1.6 1.333a1 1 0 01-.5.222l-.14.01a1 1 0 
  01-.993-.883L1 13.835V2.57a1 1 0 011-1h13.22zm-4.638 5.082c-.223.222-.53.397-.903.526A4.61 4.61 0 018.2 7.42a4.61 4.61 0 
  01-1.48-.242c-.372-.129-.68-.304-.902-.526a.45.45 0 00-.636.636c.329.33.753.571 1.246.74A5.448 5.448 0 008.2 8.32c.51 0 1.126-.068 
  1.772-.291.493-.17.917-.412 1.246-.74a.45.45 0 00-.636-.637z"></path></svg></i><i class="GHUxSkxNuJ HiSJ3Vx2WM"><svg 
  xmlns="http://www.w3.org/2000/svg" viewBox="0 0 44 22" class="chat-icon"><path d="M9.286 6.001c1.161 0 2.276.365 3.164 
  1.033.092.064.137.107.252.194.09.085.158.064.203 0 .046-.043.182-.194.251-.26.182-.17.433-.43.752-.752a.445.445 0 
  00.159-.323c0-.172-.092-.3-.227-.365A7.517 7.517 0 009.286 4C5.278 4 2 7.077 2 10.885s3.256 6.885 7.286 6.885a7.49 7.49 0 
  004.508-1.484l.022-.043a.411.411 0 00.046-.71v-.022a25.083 25.083 0 00-.957-.946.156.156 0 00-.227 0c-.933.796-2.117 1.205-3.392 1.205-2.846 
  0-5.169-2.196-5.169-4.885C4.117 8.195 6.417 6 9.286 6zm32.27 9.998h-.736c-.69 0-1.247-.54-1.247-1.209v-3.715h1.96a.44.44 0 
  00.445-.433V9.347h-2.45V7.035c-.021-.043-.066-.065-.111-.043l-1.603.583a.423.423 0 00-.29.41v1.362h-1.781v1.295c0 .238.2.433.445.433h1.337v4.19c0 
  1.382 1.158 2.505 2.583 2.505H42v-1.339a.44.44 0 00-.445-.432zm-21.901-6.62c-.739 0-1.41.172-2.013.496V4.43a.44.44 0 
  00-.446-.43h-1.788v13.77h2.234v-4.303c0-1.076.895-1.936 2.013-1.936 1.117 0 2.01.86 2.01 
  1.936v4.239h2.234v-4.561l-.021-.043c-.202-2.088-2.012-3.723-4.223-3.723zm10.054 6.785c-1.475 0-2.681-1.12-2.681-2.525 0-1.383 1.206-2.524 
  2.681-2.524 1.476 0 2.682 1.12 2.682 2.524 0 1.405-1.206 2.525-2.682 2.525zm2.884-6.224v.603a4.786 4.786 0 00-2.985-1.035c-2.533 0-4.591 
  1.897-4.591 4.246 0 2.35 2.058 4.246 4.59 4.246 1.131 0 2.194-.388 2.986-1.035v.604c0 .237.203.431.453.431h1.356V9.508h-1.356c-.25 
  0-.453.173-.453.432z"></path></svg></i></div></div></div><script defer="" crossorigin="" 
  src="https://deo.shopeemobile.com/shopee/shopee-webfepromotion-live-sg/voucher-card@stable/index.production.vouchercard-v0.21.0.js"></script></body>
"""

soup1 = BeautifulSoup(html, 'html.parser')
soup = BeautifulSoup(soup1.prettify(), 'html.parser')
# title=soup.find_all('a', {'class' ='c54pg1'})
title = soup.find_all('a')
# t2itle=soup.find_all()['title']

print(title, "\n\n\n\n\n\n\n\n")
# print(t2itle,"\n\n\n\n\n\n\n\n")

# for link in soup.find_all('a'):
#     print(link.get('href'))
