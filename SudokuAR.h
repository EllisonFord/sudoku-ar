#pragma once

#ifndef SudokuAR_H_
#define SudokuAR_H_

#include "stdafx.h"

#include <iomanip>

#include "opencv2/highgui.hpp"
#include "opencv2/imgproc.hpp"
//#include <opencv2\imgproc\imgproc_c.h>
#include <iostream>
#include <stdlib.h>
#include <stdio.h>

#include <numeric>
#include "opencv2/features2d.hpp"
#include "opencv2/calib3d/calib3d.hpp"

#include "PoseEstimation.h"

#define DELIMITERS 6

typedef struct
{
	int length;
	int nStop;
	int nStart;
	cv::Point2f vecX; // direction vector of the stripe's width
	cv::Point2f vecY; // direction vector of the stripe's length
} MyStripe;

class SudokuAR
{
public:
	SudokuAR();
	~SudokuAR();

	bool processNextFrame();
	void initVideoStream(std::string movie);
	void initVideoStream();

	bool m_feedInitialized;

private:

	bool m_playVideo;
	bool m_isFirstStripe;
	bool m_isFirstMarker;

	cv::VideoCapture m_cap;
	cv::Mat m_src, m_gray, m_blur, m_threshold, m_dst;
	
	////////////////////////////////////////////////////////////////////////

	// Contours
	//cv::Mat tmpMat;
	//IplImage tmpIpl;
	//CvMemStorage* m_memStorage = NULL; // we initialize it in the constructor
	//CvSeq* m_contours;
	//CvSeq* m_approx;
	std::vector<std::vector<cv::Point>> m_contours; // Vector for storing contour
	std::vector<cv::Vec4i> m_hierarchy;
	std::vector<cv::Point> m_approx;
	std::vector<cv::Point> m_approxChild;
	
	cv::Mat m_result;
	cv::Rect m_boundingBox;
	cv::Point *m_sudokuCorners;
	cv::Mat m_sudoku;

	static const int numberOfSides;
	static const int nOfIntervals;

	MyStripe m_stripe;
	cv::Mat m_iplStripe;

	// We will have 4 lines, one for each side of the square
	// And each line is defined by 4 floats: 2 contain the direction, 2 a point
	float m_lineParams[4 * 4];
	cv::Mat m_lineParamsMat;

	cv::Point2f m_corners[4];
	cv::Point m_markerCenter;
	cv::Mat m_iplMarker;
	int m_markerCode;
	int m_markerAngle;
	int m_distanceToMarkerInCm;

	cv::Mat m_subimages[81];
	bool m_subimagesIsImage[81];
	

	////////////////////////////////////////////////////////////////////////

	static void onBlockSizeSlider(int, void*);

	cv::Point* findSudoku();
	void processCorners();
	void computeStripe(double dx, double dy);
	cv::Point2f computeAccurateDelimiter(cv::Point p);
	cv::Point2f computeSobel(cv::Point p);
	int subpixSampleSafe(const cv::Mat& gray, const cv::Point2f& p);
	void perspectiveTransform(const cv::Point* corners);
	void orientSudokuCorners();
	void extractSubimages();

	////////////////////////////////////////////////////////////////////////

	static const cv::Scalar m_color;

	static const std::string grayWindow;
	static const std::string adaptiveThresholdWindow;
	static const std::string resultsWindow;
	static const std::string sudokuWindow;
	static const std::string trackbarsWindow;

	static const std::string thresholdTrackbarName;
	static const std::string blockSizeTrackbarName;
	static const std::string constTrackbarName;

	static const std::string houghThresholdTrackbarName;
	static const std::string minLineLengthTrackbarName;
	static const std::string maxLineGapTrackbarName;

	static const int blockSizeSliderMax;
	int m_blockSizeSlider;

	static const int constSliderMax;
	int m_constSlider;

	static const int markerThresholdSliderMax;
	int m_markerThresholdSlider;

	int m_houghThreshold;
	int m_minLineLength;
	int m_maxLineGap;

	static const std::string minAreaTrackbarName;
	static const std::string maxAreaTrackbarName;
	static const int MAX_AREA;
	int m_minArea;
	int m_maxArea;
};

#endif // !SudokuAR_H_
