function IC = ComputeIC(ciphertext, m)
%frequency_distribution = freqDist
%First split ciphertext into strings, sampling every m-th character
sub_strings = cell(1,m);
IC = zeros(1,m);
%n = length(ciphertext);
for i=1:m
    sub_strings{i} = ciphertext(i:m:end);
    distribution = freqDist(sub_strings{i});
    n = length(sub_strings{i});
    IC(i) = 1/(n*(n-1))*sum(distribution.*(distribution-1));
end