m_values = 1:8;
IC = cell(1, length(m_values));
distributions = cell(1, length(m_values));
output_filename = 'cyclic-autocorrelations.txt';
fid1 = fopen(output_filename, 'w');
for m=1:length(m_values)
    %distributions{m} = zeros(m, 26);
    distribution_this_m = zeros(m,26);
    for j=1:m
        distribution_this_m(j,:) = freqDist(ciphertext(j:m:end));
    end
    distributions{m} = distribution_this_m;
    IC{m} = ComputeIC(ciphertext, m_values(m));
    average_IC(m) = mean(IC{m});
    fprintf(fid1, 'm=%d: Autocorrelation=%1.4f\n', m, average_IC(m));
end
fclose(fid1);
distribution_m1 = distributions{1};
figure; bar(0:25, distribution_m1/sum(distribution_m1));
xlabel('Index of alphabet letter');
ylabel('Frequency of occurrence');
title('Frequency distribution of ciphertext with m=1');
distribution_m2 = distributions{2};
figure; bar(0:25, distribution_m2(1,:)/sum(distribution_m2(1,:)));
xlabel('Index of alphabet letter');
ylabel('Frequency of occurrence');
title('Frequency distribution of y_1 when m=2');
figure; bar(0:25, distribution_m2(2,:)/sum(distribution_m2(2,:)));
xlabel('Index of alphabet letter');
ylabel('Frequency of occurrence');
title('Frequency distribution of y_2 when m=2');
%Plot average values
figure; bar(m_values, average_IC);
xlabel('Shift, m');
ylabel('Average autocorrelation of y_1,...,y_m');
title('Cyclic autocorrelation testing to find Vigenere key length');