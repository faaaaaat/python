#rewrite ^/eyeglasses & sunglasses categories$ http://$host/ permanent;
#rewrite ^/(.*)-p-(\d+)\.html$ http://$host/$1-p-$2 permanent;
#rewrite ^/review-video/(.+)-(\d+)\.html$ http://$host/video-reviews/$1-$2 permanent;

if ($server_port = 80) {
    rewrite ^/favorite\.php$ http://$host/favorite permanent;
    rewrite ^/search\.php$ http://$host/search permanent;
    rewrite ^/sitemap\.html$ http://$host/sitemap permanent;
    rewrite ^/video_review\.php$ http://$host/video-reviews permanent;
    rewrite ^/customer-reviews\.html$ http://$host/customer-reviews permanent;
    rewrite ^/customer-satisfaction-feedback\.html$ http://$host/customer-satisfaction-feedback permanent;
    rewrite ^/faq\.html$ http://$host/faq permanent;
    rewrite ^/shipping-and-returns\.html$ http://$host/shipping-and-returns permanent;
    rewrite ^/about-us\.html$ http://$host/about permanent;
    rewrite ^/our-story\.html$ http://$host/our-story permanent;
    rewrite ^/social-responsibility\.html$ http://$host/social-responsibility permanent;
    rewrite ^/press-room\.html$ http://$host/press permanent;
    rewrite ^/privacy-policy\.html$ http://$host/policy permanent;
    rewrite ^/how-to-buy-prescription-eyeglasses-online\.html$ http://$host/learn/how-to-buy-prescription-eyeglasses-online permanent;
    rewrite ^/how-to-read-a-prescription\.html$ http://$host/learn/how-to-read-a-prescription permanent;
    rewrite ^/how-to-measure-your-pd\.html$ http://$host/learn/how-to-measure-your-pd permanent;
    rewrite ^/frames-and-face-shapes\.html$ http://$host/learn/frames-and-face-shapes permanent;
    rewrite ^/prescription-lens/$ http://$host/prescription-lens permanent;
    rewrite ^/prescription-lens/lens-index\.html$ http://$host/prescription-lens/lens-index permanent;
    rewrite ^/prescription-lens/premium-lens-coating\.html$ http://$host/prescription-lens/premium-lens-coating permanent;
    rewrite ^/prescription-lens/bifocal-progressive\.html$ http://$host/prescription-lens/bifocal-progressive permanent;
    rewrite ^/prescription-lens/transitions\.html$ http://$host/prescription-lens/transitions permanent;
    rewrite ^/prescription-lens/blue-cut\.html$ http://$host/prescription-lens/blue-cut permanent;
    rewrite ^/discount-coupons\.html$ http://$host/discount-coupons permanent;
    rewrite ^/cycling-sunglasses\.html$ http://$host/sunglasses/cycling permanent;
    rewrite ^/volleyball-sunglasses\.html$ http://$host/sunglasses/volleyball permanent;
    rewrite ^/retro-eyeglasses\.html$ http://$host/eyeglasses/retro permanent;
    rewrite ^/deal-of-the-week\.html$ http://$host/deal-of-the-week permanent;
    rewrite ^/sarah_palin_eyeglasses\.php$ http://$host/eyeglasses/sarah-palin permanent;
    rewrite ^/loyalty-program\.html$ http://$host/loyalty-program permanent;
    rewrite ^/(.*)-p-(\d+)\.html$ http://$host/$1-p-$2 permanent;
    rewrite ^/eyeglasses/$ http://$host/catalog permanent;
    rewrite ^/reading-glasses\.html$ http://$host/eyeglasses/reading permanent;
    rewrite ^/non-prescription-eyeglasses\.html$ http://$host/eyeglasses/non-prescription permanent;
    rewrite ^/tint-eyeglasses\.html$ http://$host/eyeglasses/tint permanent;
    rewrite ^/bogo\.html$ http://$host/bogo permanent;
    rewrite ^/eyeglasses/onsale\.html$ http://$host/eyeglasses/onsale permanent;
    rewrite ^/collections/$ http://$host/collections permanent;
    rewrite ^/collections/tortoise\.html$ http://$host/collections/tortoise permanent;
    rewrite ^/collections/cat-eye\.html$ http://$host/collections/cat-eye permanent;
    rewrite ^/collections/fall-collection-men\.html$ http://$host/collections/fall-collection-men permanent;
    rewrite ^/collections/fall-collection-women\.html$ http://$host/collections/fall-collection-women permanent;
    rewrite ^/collections/wooden\.html$ http://$host/collections/wooden permanent;
    rewrite ^/collections/urban\.html$ http://$host/collections/urban permanent;
    rewrite ^/collections/winter-collection-men\.html$ http://$host/collections/winter-collection-men permanent;
    rewrite ^/collections/winter-collection-women\.html$ http://$host/collections/winter-collection-women permanent;
    rewrite ^/collections/her-crush\.html$ http://$host/collections/her-crush permanent;
    rewrite ^/collections/his-edge\.html$ http://$host/collections/his-edge permanent;
    rewrite ^/top-10-frames-for-summer\.html$ http://$host/top-10-frames/summer permanent;
    rewrite ^/top-10-frames-for-fall\.html$ http://$host/top-10-frames/fall permanent;
    rewrite ^/top-10-frames-for-spring\.html$ http://$host/top-10-frames/spring permanent;
    rewrite ^/top-10-frames-for-winter\.html$ http://$host/top-10-frames/winter permanent;
    rewrite ^/top-10-best-selling-frames\.html$ http://$host/top-10-frames/best-selling permanent;
    rewrite ^/top-10-liked-on-facebook\.html$ http://$host/top-10-frames/liked-on-facebook permanent;
    rewrite ^/top-10-most-reviewed\.html$ http://$host/top-10-frames/most-reviewed permanent;
    rewrite ^/scan_tracking_number\.php$ http://$host/texas/index permanent;
    rewrite ^/subscribe\.php$ http://$host/subscribe permanent;
    rewrite ^/unsubscribe\.php$ http://$host/unsubscribe permanent;
    rewrite ^/promotion_over\.php$ http://$host/promotion-over permanent;
    rewrite ^/enjoy-more-for-less\.html$ http://$host/enjoy-more-for-less permanent;
    rewrite ^/back-to-school\.html$ http://$host/back-to-school permanent;
    rewrite ^/end-of-year-clearance\.html$ http://$host/end-of-year-clearance permanent;
    rewrite ^/new-year-clearance\.html$ http://$host/new-year-clearance permanent;
    rewrite ^/sitemap/$ http://$host/sitemap.xml permanent;
    rewrite ^/sitemap/catalog\.php$ http://$host/sitemap/catalog.xml permanent;
    rewrite ^/sitemap/products\.php$ http://$host/sitemap/products.xml permanent;
    rewrite ^/sitemap/site_videos\.php$ http://$host/sitemap/site-videos.xml permanent;
    rewrite ^/sitemap/product_videos\.php$ http://$host/sitemap/product-videos.xml permanent;
    rewrite ^/sitemap/videos\.php$ http://$host/sitemap/videos.xml permanent;
    rewrite ^/sitemap/images\.php$ http://$host/sitemap/images.xml permanent;
    rewrite ^/sitemap/others\.php$ http://$host/sitemap/others.xml permanent;
    rewrite ^/review-video/(.+)-(\d+)\.html$ http://$host/video-reviews/$1-$2 permanent;
    rewrite ^/order_track\.php$ http://$host/order-tracking permanent;
    rewrite ^/(.+)-a-(\d+)\.html$ http://$host/press/$1-a-$2 permanent;
    
    rewrite ^/eyeglasses(-page-\d+)?\.html$ http://$host/eyeglasses$1 permanent;
    rewrite ^/(.+)-eyeglasses(-page-\d+)?\.html http://$host/eyeglasses/$1$2 permanent;
    rewrite ^/eyeglasses-(.+)\.html$ http://$host/eyeglasses permanent;
    rewrite ^/(.+)-eyeglasses-(.+)\.html$ http://$host/eyeglasses/$1 permanent;
    rewrite ^/sunglasses(-\d+)?\.html$ http://$host/sunglasses$1 permanent;
    rewrite ^/(.+)-eyeglasses(-\d+)?\.html http://$host/sunglasses/$1$2 permanent;
    rewrite ^/sunglasses-(.+)\.html$ http://$host/sunglasses permanent;
    rewrite ^/(.+)-sunglasses-(.+)\.html$ http://$host/sunglasses/$1 permanent;
   
    #rewrite ^(.*)$ http://$host$1 permanent;
}

rewrite ^/passport\.php$ /passport permanent;
rewrite ^/logoff\.php$ /logout permanent;
rewrite ^/invoice\.php$ /invoice permanent;
rewrite ^/contact_us\.php$ /contact permanent;
rewrite ^/account\.php$ /account permanent;
rewrite ^/password_forgotten\.php$ /reset-password permanent;
rewrite ^/register\.html$ /register permanent;
rewrite ^/cart\.html$ /cart permanent;
rewrite ^/checkout\.php$ /checkout permanent;
rewrite ^/checkout_success\.php$ /thankyou permanent;
