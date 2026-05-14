`timescale 1ns/1ps

module tb_pixel_threshold;

reg [7:0] pixel;
reg [7:0] threshold;

wire out_pixel;

pixel_threshold uut(

.pixel(pixel),
.threshold(threshold),
.out_pixel(out_pixel)

);

initial begin

threshold=8'd120;

pixel=8'd50;
#10;

pixel=8'd130;
#10;

pixel=8'd200;
#10;

pixel=8'd100;
#10;

$finish;

end

endmodule