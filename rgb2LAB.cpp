#include <opencv2/opencv.hpp>

int main(int argc, const char * argv[]){
	cv::Mat src, labM;
	std::vector<cv::Mat> labPlanes;
	src = cv::imread(argv[1], 1);
	cv::cvtColor(src, labM, CV_BGR2Lab);
	split(labM, labPlanes);
	
	cv::imshow("l", labPlanes[0]);
	cv::imshow("a", labPlanes[1]);
	cv::imshow("b", labPlanes[2]);
	cv::waitKey(0);
	
	cv::imwrite("l.jpg", labPlanes[0]);
	cv::imwrite("a.jpg", labPlanes[1]);
	cv::imwrite("b.jpg", labPlanes[2]);
	
	return 0;
}