module infected_counter(

input clk,
input out_pixel,
output reg [15:0] count=0

);

always @(posedge clk)
begin

    if(out_pixel==1'b1)
        count <= count + 1;

end

endmodule