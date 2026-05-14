module pixel_threshold(

input [7:0] pixel,
input [7:0] threshold,

output reg out_pixel

);

always @(*) begin

    if(pixel > threshold)
        out_pixel = 1'b1;

    else
        out_pixel = 1'b0;

end

endmodule