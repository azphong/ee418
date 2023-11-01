M_g = ComputeShiftCorrelation(ciphertext, m);
fid2 = fopen('cyclic-cross-correlations.txt', 'w');
for i=1:m
    fprintf(fid2,'k=%d: %1.3f %1.3f %1.3f %1.3f %1.3f %1.3f %1.3f %1.3f %1.3f\n', i, M_g(i,1:9));
    fprintf(fid2,'%1.3f %1.3f %1.3f %1.3f %1.3f %1.3f %1.3f %1.3f %1.3f\n', M_g(i,10:18));
    fprintf(fid2,'%1.3f %1.3f %1.3f %1.3f %1.3f %1.3f %1.3f %1.3f\n\n', M_g(i, 19:26));
end
fclose(fid2);
figure; bar(0:25, M_g(1,:));
xlabel('Shift, k');
ylabel('Cyclic cross-correlation C');
title('Cyclic cross-correlation of y_1 when m=5');