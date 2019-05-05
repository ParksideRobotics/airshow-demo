#include <kipr/botball.h>

void draw_view() {
    int i, k;
    for(i=0; i<get_camera_width();i++){
        for(k=0;k<get_camera_height();k++){
            point2 m; m.x = i; m.y = k;
            pixel p = get_camera_pixel(m);
            graphics_pixel(i, k, p.r, p.g, p.b);
        }
    }
}

void draw_channel(int channel, int r, int g, int b){
    int objects = get_object_count(channel);
    if(objects == 0)
        return;
    int j;
    for(j=0;j<objects;j++){
        graphics_rectangle(get_object_bbox_ulx(channel, j), get_object_bbox_uly(channel, j), get_object_bbox_brx(channel, j), get_object_bbox_bry(channel, j), r, g, b);
    }
}

int main() {
    graphics_open(160, 120);
    camera_open();
    while(1==1) {
        graphics_clear();
        graphics_fill(255, 255, 255);
        if(!camera_update())
            continue;
        
        draw_view();
        draw_channel(0, 255, 0, 0);
        draw_channel(1, 255, 255, 0);
        
        graphics_update();
    }
    return 0;
}