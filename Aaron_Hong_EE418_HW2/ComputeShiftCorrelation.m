function M_g = ComputeShiftCorrelation(ciphertext, m)
M_g = zeros(m, 26);
for i=1:m
    M_g(i, :) = ComputeMg(ciphertext, m, i);
end
function Mg = ComputeMg(ciphertext, m, i)
sub_string = ciphertext(i:m:end);
distribution = freqDist(sub_string);
n = length(sub_string);
Mg = zeros(1,26);
p = [0.082 0.015 0.028 0.043 0.127 0.022 0.02 0.061 0.07 0.002 0.008 0.04 0.024...
0.067 0.075 0.019 0.001 0.06 0.063 0.091 0.028 0.01 0.023 0.001 0.02 0.001];
for j=0:25
    dist_shifted = distribution(mod((1:26)-1 + j,26)+1);
    Mg(j+1) = 1/n*sum(p.*dist_shifted);
end
