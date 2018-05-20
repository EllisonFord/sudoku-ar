/////////////////////////////////////////////////////////
//   ____  _   _ ____   ___  _  ___   _   _    ____
//  / ___|| | | |  _ \ / _ \| |/ | | | | / \  | _  \
//  \___ \| | | | | | | | | | ' /| | | |/ _ \ | |_) |
//   ___) | |_| | |_| | |_| | . \| |_| / ___ \| _  <
//  |____/ \___/|____/ \___/|_|\_\\___/ _/ \_ |_|\_ \
//
// Its BGR instead of RGB
/////////////////////////////////////////////////////////
//
// Authors:
//
// Module: TUM
// Prof.:
// Sup.:
//
/////////////////////////////////////////////////////////

#include "stdafx.h"
#include <opencv2/opencv.hpp>
#include <opencv2/core.hpp>
#include <opencv2/highgui.hpp>
#include "sudoku_ar.h"
using namespace std;
using namespace cv;

const int fps = 20;
const string source_stream = "C:/Users/Administrator/Documents/MEGA/Robotics TUM/Augmented Reality/Woche_2/MarkerMovie.MP4";
//const int source_stream = 0; // default webcam

void checkStream(VideoCapture& vid) {

	if (vid.isOpened())
		vid.release();

	vid.open(source_stream); // open the default camera
	if (vid.isOpened() == false) {
		cout << "No webcam found, using a video file" << endl;
		vid.open("MarkerMovie.mpg");
		if (vid.isOpened() == false) {
			cout << "No video file found. Exiting." << endl;
			exit(0);
		}
	}
}


int main(int argc, char* argv[])
{
	VideoCapture vid(source_stream);
	
	checkStream(vid);
	
	Mat source, gray, filtered;
	
	const string kWinSource = "Colour Feed";
	const string kWinGray = "Gray Scale Image";
	const string kWinFiltered = "Filtered Stream";

	namedWindow(kWinSource, WINDOW_FREERATIO);
	namedWindow(kWinGray, WINDOW_FREERATIO);
	namedWindow(kWinFiltered, WINDOW_FREERATIO);

	while (vid.read(source)) {

		// pushing the vid frame into the Mat object
		//vid >> frame

		// Turn colour to Grayscale
		cvtColor(source, gray, CV_BGR2GRAY);

		/* Different threshold methods */
		//threshold(gray, filtered, 120, 255, CV_THRESH_BINARY);
		adaptiveThreshold(gray, filtered, 255, ADAPTIVE_THRESH_MEAN_C, THRESH_BINARY, 33, 5);
		//adaptiveThreshold(gray, filtered, 255, ADAPTIVE_THRESH_GAUSSIAN_C, THRESH_BINARY, 33, 5);

		// Open 3 different windows
		imshow(kWinSource, source);
		imshow(kWinGray, gray);
		imshow(kWinFiltered, filtered);

		int key = waitKey(1000/fps); // this determines the frames per second
		if (key == 27) break;

	}

}
