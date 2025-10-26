# -*- coding: utf-8 -*-


flashcard_data = {
    "画像処理(Image Processing)": "画像を入力とし、ノイズ除去や明るさ調整など何らかの処理を施し、出力が再び画像であるタイプの処理を指す。",
    "コンピュータビジョン (Computer Vision)": "入力された画像から3次元の世界を復元したり、そこに写っている対象に関する情報を抽出・理解したりする処理。人間の視覚機能をコンピュータで実現することを目指す。",
    "コンピュータグラフィックス (Computer Graphics)": "実際のカメラの代わりに、コンピュータ内にある3次元の記述 (モデル) から画像を生成する技術であり、コンピュータビジョンの技術とは逆の関係にあるとみなされる。",
    "透視投影モデル (Perspective Projection Model)": "コンピュータビジョン分野で利用されるモデルで、光学中心から透明な仮想投影面を通して3次元空間を見ることとして、結像をモデル化する。",
    "消失点(Vanishing Point)": "3次元空間で平行な線群が、透視投影によって2次元の画像平面上で一点に収束して見える点.3次元復元や幾何学的補正に利用される。",
    "画角(Angle of View)": "カメラとレンズを選定したときに決定する撮影範囲のことであり、撮像素子サイズが大きいほど広い範囲を撮影できる。",
    "撮像素子(Image Sensor)": "レンズで集められた光の明るさの分布を、電圧信号として取り出す (光強度を標本化する) 2次元的に並んだ受光素子。",
    "フレームレート (Frame Rate)": "1秒あたりに切り替えて表示する画像枚数のことであり、時系列画像を時間方向に標本化する周波数に対応する。",
    "画素(Pixel)": "ディジタル画像を構成する最小単位の要素である.横M個 縦N個の画素で構成される画像の総数は MN個である。",
    "グレースケール画像 (Grayscale Image)": "画素値が、画像中の位置に対応する明るさ(濃淡) だけを表す画像である.通常,8ビット (0~255) で表現されることが多い。",
    "プロファイル (Profile)": "横軸に画像上の位置、縦軸に画素値をとったグラフであり、画像中のある行または列における画素値の変化を把握しやすくするもの。",
    "標本化(Sampling)": "アナログ信号(連続的な光強度)を 一定の間隔で配置された標本点における離散的なアナログ値として取り出す処理。",
    "標本点(Sampling Point)": "画像の標本化において、縦横に等間隔の格子状に配置され、光強度を電圧値として取り出す位置。",
    "標本化間隔(Sampling Interval)": "標本化において、標本点同士が縦横に配置される等間隔の距離、これが画素のサイズに相当する。",
    "標本値(Sampling Value)": "標本点におけるアナログ値そのもののことであり、撮像素子からアナログの電圧信号として出力される。",
    "量子化(Quantization)": "標本値(アナログ値)を有限分解能の数値(画素値)に変換する処理であり、A/D変換器によって行われる。",
    "量子レベル (Quantization Level)": "量子化によって標本値が取りうる段階の数のことであり,8ビット量子化では256段階となる。",
    "標本化定理(Sampling Theorem)": "アナログ信号が周波数 $f_{max}$ に帯域制限されているとき,2$f_{max}$ 以上の標本化周波数で標本化すれば情報を失わないという定理。",
    "エイリアシング (Aliasing)": "標本化定理を満たさないとき、標本値に元の信号とは異なる偽信号 (alias) が現れる現象。",
    "擬似輪郭(False Contour)": "元の画像にはなかった等高線のような境界(画素値の階段状の変化)が量子化誤差によってディジタル画像に現れる現象。",
    "量子化雑音(Quantization Noise)": "量子化の際に生じる丸め誤差(量子化誤差)によってディジタル画像に現れる画素値の歪み。",
    "時系列画像(Time series images)": "1枚のグレースケール画像を時間方向に並べたものであり、フレームレートに対応する標本化周波数で時間方向に標本化と量子化を行った結果。",
    "階調変換関数 (Gray-level transformation function)": "入力画像のそれぞれの画素値に対し、出力画像の画素値をどのように対応づけるかを指定する関数。",
    "トーンカーブ (Tone Curve)": "階調変換関数をグラフで表したもの。曲線形状を変更することで、画像の明るさやコントラストを視覚的に調整できる。",
    "ガンマ変換 (Gamma Transformation)": "累乗型のトーンカーブ: $y=255(\\frac{x}{255})^{\\frac{1}{\\gamma}}$ を用いた濃淡変換であり、$\\gamma$ の値によって画像の明るさの応答特性を変える処理。",
    "ヒストグラム平坦化 (Histogram Equalization)": "画像のヒストグラムの偏りを自動的に補正し、その分布を平坦化することで、画像のコントラストを全体的に向上させる手法。",
    "疑似カラー (Pseudo Color)": "グレースケール画像の画素値をR, G, B各チャンネルの値とし、それぞれに異なるトーンカーブを用いることで擬似的に色をつける処理。",
    "画像間演算 (Inter-image Operation)": "2枚またはそれ以上の枚数の入力画像を用い、それぞれの画像の同じ位置にある画素ごとに、あらかじめ決められた演算を行う処理。",
    "アルファブレンディング (Alpha Blending)": "2枚の画像を重ね合わせる際、重み $\\alpha$ $(0\\le \\alpha \\le 1)$ を用いて各画素の寄与度を調整する処理。",
    "ディゾルブ (Dissolve)": "動画像において、$\\alpha$ の値を時間的に変化させることにより、あるシーンから別のシーンへ徐々に変化させていく手法。",
    "オーバーラップ (Overlap)": "動画像においてシーンを切り替える手法として、ディゾルブと同じ手法を指すことがある。",
    "フェード (Fade)": "ディゾルブの一種であり、特に黒や白を一度経由するディゾルブを指す。",
    "マスク処理 (Mask Operation)": "2枚の画像を合成する際、マスク画像を用いて、どの部分をどちらの画像から取り込むかを画素ごとに指定する処理。",
    "マスク画像 (Mask Image)": "2枚の画像を合成する際に、どの画素をどちらの画像から取り込むかを指定するために、あらかじめ作成される画像(通常は1と0で指定)。",
    "マスク合成 (Mask Compositing)": "マスク処理と同義であり、マスク画像の情報に基づいて画像を合成し、前景と背景の領域を明確に切り分けて画像を構成する。",
    "可視光 (Visible Light)": "人間が知覚することのできる波長範囲の電磁波である(人間の目に見える範囲の光のこと)。",
    "紫外線(Ultraviolet Ray)": "紫として知覚する波長よりも短く、人間が知覚できない電磁波である。",
    "赤外線(Infrared Ray)": "赤として知覚する波長よりも長く、人間が知覚できない電磁波である。",
    "混色 (Colour Mixing)": "色を混ぜ合わせることであり、加法混色と減法混色の2種類がある。",
    "加法混色 (Additive Colour Mixing)": "異なる色の光を混ぜ合わせて新しい色を作り出す方法である。",
    "減法混色 (Subtractive Colour Mixing)": "絵の具やインクなどの色材を混ぜることで、色が暗くなる現象である。",
    "RGBカラー画像(RGB Color Image)": "画像中の位置に対応した赤・緑・青の3つの画素値をもつカラー画像である。",
    "ヒストグラム (Histogram)": "横軸に画素値を、縦軸にその画素値を持つ画素の頻度(個数)をとり、画素値の分布を棒グラフで表したもの。",
    "最小値・最大値 (Minimum/Maximum Value)": "ある画像の画素値のなかで、最も小さいものを最小値、最も大きいものを最大値とよぶ。",
    "平均値(Mean)": "画像サイズ $M \\times N$ 画素の画像の平均值であり、次の式で求めることができる: $Mean=\\frac{1}{M\\times N}\\sum_{x=0}^{M-1}\\sum_{y=0}^{N-1}p(x,y)$。",
    "中央値 (Median)": "画像のヒストグラムを求め、画素値の小さいほうから $MN/2$ 番目の画素値。",
    "最頻値 (Mode)": "画像のヒストグラムを求め、最も頻度が高い (度数が高い) 画素値。",
    "分散 (Variance)": "画像サイズ $M \\times N$ 画素の分散であり、次の式で計算される: $\\sigma^{2}=\\frac{1}{M\\times N}\\sum_{i=1}^{M}\\sum_{j=1}^{N}p_{ij}^{2}-(\\frac{1}{M\\times N}\\sum_{i=1}^{M}\\sum_{j=1}^{N}p_{ij})^{2}$。",
    "6角錐モデル - HSV (Hexcone Model - HSV)": "色相 (Hue)、彩度(Saturation)、明度(Value) の3つの要素で色を表現する HSVカラーモデルを、六角錐の立体で視覚化したもの。",
    "空間フィルタリング/空間フィルタ (Spatial Filtering / Spatial Filter)": "出力画像のある1画素の値を求めるために、入力画像の対応する画素値だけではなく、その周囲の画素も含めた領域内の画素値を用いて計算する処理のこと。この処理を空間フィルタリング、そこで用いられるフィルタを空間フィルタとよぶ。",
    "線形フィルタ (Linear Filter)": "空間フィルタの一種で、複数の周囲画素から1つの出力画素を重み付和で計算するフィルタ。式: $g(i,j)=\\sum_{m=-W}^{W}\\sum_{n=-W}^{W}f(i+m,j+n)h(m,n)$。",
    "非線形フィルタ (Nonlinear Filter)": "線形フィルタの手順にあてはまらない処理をともなうフィルタ。線形フィルタが重ね合わせの原理に従うのに対し、非線形フィルタはそうではないため、より複雑な処理が可能。",
    "平滑化(Smoothing)": "ぼけた画像のように滑らかな濃淡変化を画像に与える処理。画像に含まれるノイズなどの不要な濃淡変動を軽減するためにも用いられる。",
    "平均化フィルタ (Averaging Filter)": "フィルタによって覆われる領域内の画素値の平均値を求めるフィルタ。例: 3x3画素のフィルタで、すべての係数が $1/9$ のもの。",
    "重み付き平均化/加重平均化フィルタ (Weighted Averaging / Weighted Averaging Filter)": "単純な平均化ではなく、「自分自身の画素(フィルタの中心)に近いほど重み大、遠いほど重み小」なフィルタ (加重平均化フィルタ)を使って平均化をすること。",
    "ガウシアンフィルタ (Gaussian Filter)": "加重平均化フィルタの一種で、その重みをガウス分布に基づけたもの。2次元ガウス分布の式: $h_{\\epsilon}(x,y)=\\frac{1}{2\\pi\\sigma^{2}}exp(-\\frac{x^{2}+y^{2}}{2\\sigma^{2}})$。",
    "特定方向への平滑化 (Smoothing in a Specific Direction)": "ノイズ除去やぼかしを行う際に、特定の方向(例:水平、垂直、対角)にのみ平滑化処理を適用する方法。",
    "エッジ抽出 (Edge Extraction)": "画像中で明るさが急に変化するエッジ部分を取り出すこと。",
    "微分フィルタ (Derivative Filter)": "ディジタル画像の場合、微分は注目画素とその隣接画素との差分で置き換えられる。一例 (横方向の差分の平均) のフィルタは: $\\begin{pmatrix} 0 & 0 & 0 \\\\ -1/2 & 0 & 1/2 \\\\ 0 & 0 & 0 \\end{pmatrix}$",
    "プリューウィットフィルタ (Prewitt Filter)": "横方向の微分と縦方向の平滑化 (縦3画素の平均化処理など) を組み合わせ、ノイズを抑えながらエッジを抽出するフィルタ。横方向のフィルタの数値例: $\\begin{pmatrix} -1 & 0 & 1 \\\\ -1 & 0 & 1 \\\\ -1 & 0 & 1 \\end{pmatrix}$。",
    "ソーベルフィルタ (Sobel Filter)": "プリューウィットフィルタと同様に微分と平滑化を組み合わせるが、縦方向の平滑化のときに重みを付けた平均化を行うフィルタ。横方向のフィルタの数値例: $\\begin{pmatrix} -1 & 0 & 1 \\\\ -2 & 0 & 2 \\\\ -1 & 0 & 1 \\end{pmatrix}$。",
    "2次微分フィルタ (Second Derivative Filter)": "微分を2回繰り返す (差分を2回繰り返す) 処理。これにより「画素値の変化度合いの大小」が得られ、エッジを1次微分より正確に得ることができる。",
    "ラプラシアンフィルタ (Laplacian Filter)": "横方向の2次微分の結果と縦方向の2次微分の結果を足し合わせる処理と等価な1つのフィルタ。例: $\\begin{pmatrix} 0 & 1 & 0 \\\\ 1 & -4 & 1 \\\\ 0 & 1 & 0 \\end{pmatrix}$。",
    "エッジ検出(Edge Detection)": "空間フィルタリングによるエッジ抽出処理の出力(実数値の画像)から、どの画素がエッジに相当するのかを特定するために、さらに行う処理。",
    "鮮鋭化(Sharpening)": "元の画像の濃淡を残したままエッジを強調する処理。平滑化とは反対に、元の画像の画素値変化(濃淡変化)を大きくする変換。",
    "メディアンフィルタ (Median Filter)": "画素値の平均の代わりに、ある領域内の中央値(メディアン) を出力とするフィルタ。スパイク状のノイズの除去にたいへん効果がある。",
    "最大値フィルタ (Maximum Value Filter)": "周辺の画素値を比較し、その中で最も大きい値で置き換えるフィルタ。明るいノイズ(白っぽい点など)を除去する効果があり、膨張フィルタとも呼ばれる。",
    "最小値フィルタ (Minimum Value Filter)": "周辺の画素値を比較し、その中で最も小さい値で置き換えるフィルタ。暗いノイズ(黒い点など)を除去する効果があり、収縮フィルタとも呼ばれる。"
}

english_translations = {
    "画像処理(Image Processing)": {
        "question": "Image Processing",
        "answer": "Refers to a type of processing where an image is the input, some operation like noise removal or brightness adjustment is applied, and the output is an image again."
    },
    "コンピュータビジョン (Computer Vision)": {
        "question": "Computer Vision",
        "answer": "The processing of extracting and understanding information about objects in an image, often aiming to reconstruct or comprehend the 3D world from the input image. The goal is to realize human visual functions on a computer."
    },
    "コンピュータグラフィックス (Computer Graphics)": {
        "question": "Computer Graphics",
        "answer": "A technique that generates an image from a 3D description (model) within a computer, instead of an actual camera, and is considered to have an inverse relationship with computer vision technology."
    },
    "透視投影モデル (Perspective Projection Model)": {
        "question": "Perspective Projection Model",
        "answer": "A model used in computer vision that simulates image formation by viewing 3D space from an optical center through a transparent virtual projection plane."
    },
    "消失点(Vanishing Point)": {
        "question": "Vanishing Point",
        "answer": "A point where parallel lines in three-dimensional space appear to converge on a two-dimensional image plane through perspective projection. Used in 3D reconstruction and geometric correction."
    },
    "画角(Angle of View)": {
        "question": "Angle of View",
        "answer": "The range of capture determined when selecting a camera and lens; a larger image sensor size allows for a wider area to be photographed."
    },
    "撮像素子(Image Sensor)": {
        "question": "Image Sensor",
        "answer": "A 2D array of light-receiving elements that converts the distribution of light intensity focused by the lens into an electrical voltage signal (sampling the light intensity)."
    },
    "フレームレート (Frame Rate)": {
        "question": "Frame Rate",
        "answer": "The number of images switched and displayed per second, corresponding to the temporal sampling frequency for time-series images."
    },
    "画素(Pixel)": {
        "question": "Pixel",
        "answer": "The smallest constituent element of a digital image. The total number of pixels is $M \\times N$ for an image composed of $M$ horizontal and $N$ vertical pixels."
    },
    "グレースケール画像 (Grayscale Image)": {
        "question": "Grayscale Image",
        "answer": "An image where the pixel value represents only the brightness (intensity or gray level) corresponding to its position in the image. It is usually expressed in 8 bits (0 to 255)."
    },
    "プロファイル (Profile)": {
        "question": "Profile",
        "answer": "A graph where the horizontal axis represents image position and the vertical axis represents pixel value, making it easier to grasp the change in pixel values along a specific row or column."
    },
    "標本化(Sampling)": {
        "question": "Sampling",
        "answer": "The process of extracting discrete analog values from an analog signal (continuous light intensity) at sample points spaced at regular intervals."
    },
    "標本点(Sampling Point)": {
        "question": "Sampling Point",
        "answer": "The locations arranged in a regular grid pattern where light intensity is extracted as a voltage value during image sampling."
    },
    "標本化間隔(Sampling Interval)": {
        "question": "Sampling Interval",
        "answer": "In sampling, the equal distance between sample points both vertically and horizontally. This corresponds to the size of a pixel."
    },
    "標本値(Sampling Value)": {
        "question": "Sampling Value",
        "answer": "The analog value itself at a sampling point, outputted as an analog voltage signal from the image sensor."
    },
    "量子化(Quantization)": {
        "question": "Quantization",
        "answer": "The process of converting the analog sampling value into a numerical value with finite resolution (the pixel value), performed by the A/D converter."
    },
    "量子レベル (Quantization Level)": {
        "question": "Quantization Level",
        "answer": "The number of discrete steps the sampled value can take after quantization; for example, 8-bit quantization yields 256 levels."
    },
    "標本化定理(Sampling Theorem)": {
        "question": "Sampling Theorem",
        "answer": "The theorem stating that information in an analog signal limited to a maximum frequency $f_{max}$ will not be lost if sampled at a frequency of $2f_{max}$ or greater."
    },
    "エイリアシング (Aliasing)": {
        "question": "Aliasing",
        "answer": "The phenomenon where a false signal (alias), different from the original signal, appears in the sampled values when the sampling theorem conditions are not met."
    },
    "擬似輪郭(False Contour)": {
        "question": "False Contour",
        "answer": "The phenomenon where contour-like boundaries (step-like changes in pixel value) not present in the original analog image appear in the digital image due to quantization error."
    },
    "量子化雑音(Quantization Noise)": {
        "question": "Quantization Noise",
        "answer": "The distortion of pixel values that appears in a digital image caused by the rounding error (quantization error) generated during quantization."
    },
    "時系列画像(Time series images)": {
        "question": "Time series images",
        "answer": "A sequence of grayscale images aligned in the time direction, resulting from sampling and quantization in the time direction at a frequency corresponding to the frame rate."
    },
    "階調変換関数 (Gray-level transformation function)": {
        "question": "Gray-level transformation function",
        "answer": "A function that specifies the mapping relationship between the pixel values of an input image and the corresponding pixel values of the output image."
    },
    "トーンカーブ (Tone Curve)": {
        "question": "Tone Curve",
        "answer": "A graphical representation of the gray-level transformation function. Changing the curve's shape visually adjusts the image's brightness and contrast."
    },
    "ガンマ変換 (Gamma Transformation)": {
        "question": "Gamma Transformation",
        "answer": "A tonal transformation using a power-law tone curve: $y=255(\\frac{x}{255})^{\\frac{1}{\\gamma}}$ that changes the image's brightness response characteristic based on the value of $\\gamma$."
    },
    "ヒストグラム平坦化 (Histogram Equalization)": {
        "question": "Histogram Equalization",
        "answer": "A method to automatically correct the non-uniform distribution of an image's histogram by flattening it, thereby globally improving the image contrast."
    },
    "疑似カラー (Pseudo Color)": {
        "question": "Pseudo Color",
        "answer": "A process of applying artificial color to a grayscale image by taking its pixel values as the R, G, and B channels and applying suitably different tone curves to each channel."
    },
    "画像間演算 (Inter-image Operation)": {
        "question": "Inter-image Operation",
        "answer": "An operation performed on two or more input images where a defined calculation is carried out element-wise (pixel-by-pixel) at the same location across all images."
    },
    "アルファブレンディング (Alpha Blending)": {
        "question": "Alpha Blending",
        "answer": "A process that combines two images using a weighting factor $(\\alpha, \text{ where } 0\\le \\alpha \\le 1)$ to adjust the contribution of each image's pixel value."
    },
    "ディゾルブ (Dissolve)": {
        "question": "Dissolve",
        "answer": "A technique in video where the value of $\\alpha$ is varied temporally to gradually transition from one scene to another."
    },
    "オーバーラップ (Overlap)": {
        "question": "Overlap",
        "answer": "A term often used synonymously with 'dissolve' to refer to the method of temporally overlapping video scenes to transition between them."
    },
    "フェード (Fade)": {
        "question": "Fade",
        "answer": "A type of dissolve that specifically transitions through a uniform black or white screen."
    },
    "マスク処理 (Mask Operation)": {
        "question": "Mask Operation",
        "answer": "The process of combining two images using a mask image to specify, pixel by pixel, which parts should be taken from which source image."
    },
    "マスク画像 (Mask Image)": {
        "question": "Mask Image",
        "answer": "An image (typically created using values of 1 or 0) prepared in advance to specify, pixel by pixel, which parts of the source images should be used in the final composite."
    },
    "マスク合成 (Mask Compositing)": {
        "question": "Mask Compositing",
        "answer": "Synonymous with 'Mask Operation,' this refers to combining images based on mask data to clearly define and integrate foreground and background regions into a final composite."
    },
    "可視光 (Visible Light)": {
        "question": "Visible Light",
        "answer": "Electromagnetic waves within the wavelength range that can be perceived by humans (The range of light that can be seen by the human eye)."
    },
    "紫外線(Ultraviolet Ray)": {
        "question": "Ultraviolet Ray",
        "answer": "Electromagnetic waves with a shorter wavelength than the perceived color violet, which cannot be perceived by humans."
    },
    "赤外線(Infrared Ray)": {
        "question": "Infrared Ray",
        "answer": "Electromagnetic waves with a longer wavelength than the perceived color red, which cannot be perceived by humans."
    },
    "混色 (Colour Mixing)": {
        "question": "Colour Mixing",
        "answer": "The process of mixing colors, which includes two types: additive colour mixing and subtractive colour mixing."
    },
    "加法混色 (Additive Colour Mixing)": {
        "question": "Additive Colour Mixing",
        "answer": "The process of mixing different colors of light to create new colors."
    },
    "減法混色 (Subtractive Colour Mixing)": {
        "question": "Subtractive Colour Mixing",
        "answer": "The phenomenon in which colors become darker when colorants such as paints and inks are mixed."
    },
    "RGBカラー画像(RGB Color Image)": {
        "question": "RGB Color Image",
        "answer": "A color image that has three pixel values (Red, Green, Blue) corresponding to the position in the image."
    },
    "ヒストグラム (Histogram)": {
        "question": "Histogram",
        "answer": "A bar graph representing the distribution of pixel values, where the horizontal axis is the pixel value and the vertical axis is the frequency (number) of pixels having that value."
    },
    "最小値・最大値 (Minimum/Maximum Value)": {
        "question": "Minimum/Maximum Value",
        "answer": "In an image's pixel values, the smallest value is called the minimum value, and the largest is called the maximum value."
    },
    "平均値(Mean)": {
        "question": "Mean Value",
        "answer": "The mean of an $M \\times N$ pixel image, calculated by the sum of all pixel values divided by the total number of pixels: $Mean=\\frac{1}{M\\times N}\\sum_{x=0}^{M-1}\\sum_{y=0}^{N-1}p(x,y)$."
    },
    "中央値 (Median)": {
        "question": "Median Value",
        "answer": "Determined from the image's histogram, it is the $MN/2$-th pixel value when sorted from the smallest pixel value."
    },
    "最頻値 (Mode)": {
        "question": "Mode Value",
        "answer": "The pixel value with the highest frequency (highest count) when determined from the image's histogram."
    },
    "分散 (Variance)": {
        "question": "Variance",
        "answer": "The variance of an $M \\times N$ pixel image, calculated by the formula: $\\sigma^{2}=\\frac{1}{M\\times N}\\sum_{i=1}^{M}\\sum_{j=1}^{N}p_{ij}^{2}-(\\frac{1}{M\\times N}\\sum_{i=1}^{M}\\sum_{j=1}^{N}p_{ij})^{2}$."
    },
    "6角錐モデル - HSV (Hexcone Model - HSV)": {
        "question": "Hexcone Model - HSV",
        "answer": "A three-dimensional visualization of the HSV color model, which represents colors using three components: Hue, Saturation, and Value."
    },
    "空間フィルタリング/空間フィルタ (Spatial Filtering / Spatial Filter)": {
        "question": "Spatial Filtering / Spatial Filter",
        "answer": "A process that calculates the value of a single pixel in the output image by using the pixel values within a region of the input image, including not only the corresponding pixel but also its surrounding pixels. The filter used is called a spatial filter."
    },
    "線形フィルタ (Linear Filter)": {
        "question": "Linear Filter",
        "answer": "A type of spatial filter that computes one output pixel as a weighted sum of multiple surrounding pixels using the formula: $g(i,j)=\\sum_{m=-W}^{W}\\sum_{n=-W}^{W}f(i+m,j+n)h(m,n)$."
    },
    "非線形フィルタ (Nonlinear Filter)": {
        "question": "Nonlinear Filter",
        "answer": "Any filter that involves processing not conforming to the linear filter procedure. Unlike linear filters, they do not follow the principle of superposition, allowing for more complex processing."
    },
    "平滑化(Smoothing)": {
        "question": "Smoothing",
        "answer": "A process that imparts smooth tonal changes to an image, similar to an out-of-focus image. It is also used to reduce unwanted tonal variations such as noise."
    },
    "平均化フィルタ (Averaging Filter)": {
        "question": "Averaging Filter",
        "answer": "A filter that computes the average value of the pixel values within the region covered by the filter. Example: A $3\\times3$ pixel filter where all coefficients are $1/9$."
    },
    "重み付き平均化/加重平均化フィルタ (Weighted Averaging / Weighted Averaging Filter)": {
        "question": "Weighted Averaging / Weighted Averaging Filter",
        "answer": "Averaging using a filter where 'the closer to the pixel itself (the filter's center), the greater the weight, and the farther away, the smaller the weight'."
    },
    "ガウシアンフィルタ (Gaussian Filter)": {
        "question": "Gaussian Filter",
        "answer": "A type of weighted averaging filter where the weights are based on the Gaussian distribution. The 2D Gaussian distribution formula is: $h_{\\epsilon}(x,y)=\\frac{1}{2\\pi\\sigma^{2}}exp(-\\frac{x^{2}+y^{2}}{2\\sigma^{2}})$."
    },
    "特定方向への平滑化 (Smoothing in a Specific Direction)": {
        "question": "Smoothing in a Specific Direction",
        "answer": "A filtering technique used in image processing to reduce noise or blur only along a chosen direction (e.g., horizontal, vertical, or diagonal)."
    },
    "エッジ抽出 (Edge Extraction)": {
        "question": "Edge Extraction",
        "answer": "The process of extracting edge portions where brightness changes suddenly in an image."
    },
    "微分フィルタ (Derivative Filter)": {
        "question": "Derivative Filter",
        "answer": "In digital images, the derivative is replaced by the difference between a target pixel and its adjacent pixel. Example (average of left/right differences) filter: $\\begin{pmatrix} 0 & 0 & 0 \\\\ -1/2 & 0 & 1/2 \\\\ 0 & 0 & 0 \\end{pmatrix}$."
    },
    "プリューウィットフィルタ (Prewitt Filter)": {
        "question": "Prewitt Filter",
        "answer": "A filter that combines horizontal differentiation and vertical smoothing (e.g., 3-pixel averaging) to extract edges while suppressing noise. Example of the horizontal filter's numerical representation: $\\begin{pmatrix} -1 & 0 & 1 \\\\ -1 & 0 & 1 \\\\ -1 & 0 & 1 \\end{pmatrix}$."
    },
    "ソーベルフィルタ (Sobel Filter)": {
        "question": "Sobel Filter",
        "answer": "Similar to the Prewitt filter, it combines differentiation and smoothing but applies weighted averaging during vertical smoothing. Example of the horizontal filter's numerical representation: $\\begin{pmatrix} -1 & 0 & 1 \\\\ -2 & 0 & 2 \\\\ -1 & 0 & 1 \\end{pmatrix}$."
    },
    "2次微分フィルタ (Second Derivative Filter)": {
        "question": "Second Derivative Filter",
        "answer": "A process that repeats differentiation twice (repeats differencing twice). This yields the 'magnitude of the change in pixel value,' allowing edges to be obtained more accurately than with the first derivative."
    },
    "ラプラシアンフィルタ (Laplacian Filter)": {
        "question": "Laplacian Filter",
        "answer": "A single filter equivalent to the process of adding the result of the horizontal second derivative and the vertical second derivative. Example: $\\begin{pmatrix} 0 & 1 & 0 \\\\ 1 & -4 & 1 \\\\ 0 & 1 & 0 \\end{pmatrix}$."
    },
    "エッジ検出(Edge Detection)": {
        "question": "Edge Detection",
        "answer": "Further processing performed to identify which pixels in the real-number output image from spatial filtering correspond to edges."
    },
    "鮮鋭化(Sharpening)": {
        "question": "Sharpening",
        "answer": "A process that enhances edges while preserving the original image's tones. It is a transformation opposite to smoothing, increasing the pixel value changes (tonal changes) of the original image."
    },
    "メディアンフィルタ (Median Filter)": {
        "question": "Median Filter",
        "answer": "A filter that outputs the median (central) value within a certain region, instead of the average pixel value. It is highly effective at removing spike-like noise."
    },
    "最大値フィルタ (Maximum Value Filter)": {
        "question": "Maximum Value Filter",
        "answer": "A filter that compares surrounding pixel values and replaces the pixel value with the largest value among them. It is effective at removing bright noise (whitish dots) and is also called an expansion (dilation) filter."
    },
    "最小値フィルタ (Minimum Value Filter)": {
        "question": "Minimum Value Filter",
        "answer": "A filter that compares surrounding pixel values and replaces the pixel value with the smallest value among them. It is effective at removing dark noise (black dots) and is also called a contraction (erosion) filter."
    }
}

thai_translations = {
    "画像処理(Image Processing)": {
        "question": "การประมวลผลภาพ (Image Processing)",
        "answer": "การประมวลผลที่มีภาพเป็นข้อมูลนำเข้า ดำเนินการปรับปรุงบางอย่าง เช่น การลดสัญญาณรบกวนหรือการปรับความสว่าง และมีผลลัพธ์เป็นภาพอีกครั้ง"
    },
    "コンピュータビジョン (Computer Vision)": {
        "question": "คอมพิวเตอร์วิทัศน์ (Computer Vision)",
        "answer": "การประมวลผลเพื่อดึงและทำความเข้าใจข้อมูลเกี่ยวกับวัตถุในภาพ มักมีเป้าหมายเพื่อสร้างโลก 3 มิติจากภาพนำเข้า หรือทำความเข้าใจสิ่งที่ปรากฏ มีเป้าหมายเพื่อทำให้การทำงานของสายตามนุษย์เกิดขึ้นบนคอมพิวเตอร์"
    },
    "コンピュータグラフィックス (Computer Graphics)": {
        "question": "คอมพิวเตอร์กราฟิกส์ (Computer Graphics)",
        "answer": "เทคนิคที่สร้างภาพจากคำอธิบาย 3 มิติ (แบบจำลอง) ภายในคอมพิวเตอร์ แทนการใช้กล้องจริง และถือว่าเป็นความสัมพันธ์ผกผันกับเทคโนโลยีคอมพิวเตอร์วิทัศน์"
    },
    "透視投影モデル (Perspective Projection Model)": {
        "question": "แบบจำลองการฉายภาพแบบทัศนียภาพ (Perspective Projection Model)",
        "answer": "แบบจำลองที่ใช้ในสาขาคอมพิวเตอร์วิทัศน์ ซึ่งจำลองการเกิดภาพโดยมองพื้นที่ 3 มิติจากศูนย์กลางเชิงแสงผ่านระนาบการฉายภาพเสมือนที่โปร่งใส"
    },
    "消失点(Vanishing Point)": {
        "question": "จุดรวมสายตา (Vanishing Point)",
        "answer": "จุดที่กลุ่มเส้นขนานในพื้นที่ 3 มิติปรากฏว่ามาบรรจบกันเป็นจุดเดียวบนระนาบภาพ 2 มิติผ่านการฉายภาพแบบทัศนียภาพ ใช้ในการสร้าง 3 มิติและการแก้ไขทางเรขาคณิต"
    },
    "画角(Angle of View)": {
        "question": "มุมมองภาพ (Angle of View)",
        "answer": "ขอบเขตการถ่ายภาพที่กำหนดเมื่อเลือกกล้องและเลนส์ โดยที่ขนาดของเซนเซอร์รับภาพที่ใหญ่ขึ้นจะช่วยให้สามารถถ่ายภาพในพื้นที่ที่กว้างขึ้นได้"
    },
    "撮像素子(Image Sensor)": {
        "question": "เซนเซอร์รับภาพ (Image Sensor)",
        "answer": "อาร์เรย์ขององค์ประกอบรับแสง 2 มิติที่เปลี่ยนการกระจายความเข้มของแสงที่รวมกันโดยเลนส์ให้เป็นสัญญาณแรงดันไฟฟ้า (การสุ่มความเข้มของแสง)"
    },
    "フレームレート (Frame Rate)": {
        "question": "อัตราเฟรม (Frame Rate)",
        "answer": "จำนวนภาพที่เปลี่ยนและแสดงผลต่อวินาที ซึ่งสอดคล้องกับความถี่การสุ่มตามเวลาสำหรับภาพอนุกรมเวลา"
    },
    "画素(Pixel)": {
        "question": "พิกเซล (Pixel)",
        "answer": "องค์ประกอบที่เล็กที่สุดที่ประกอบเป็นภาพดิจิทัล จำนวนพิกเซลทั้งหมดคือ $M \\times N$ สำหรับภาพที่ประกอบด้วย $M$ พิกเซลในแนวนอนและ $N$ พิกเซลในแนวตั้ง"
    },
    "グレースケール画像 (Grayscale Image)": {
        "question": "ภาพโทนสีเทา (Grayscale Image)",
        "answer": "ภาพที่ค่าพิกเซลแสดงเฉพาะความสว่าง (ความเข้ม) ที่สอดคล้องกับตำแหน่งในภาพ โดยปกติจะแสดงด้วย 8 บิต (0 ถึง 255)"
    },
    "プロファイル (Profile)": {
        "question": "โปรไฟล์ (Profile)",
        "answer": "กราฟที่มีแกนนอนเป็นตำแหน่งบนภาพและแกนตั้งเป็นค่าพิกเซล ทำให้ง่ายต่อการทำความเข้าใจการเปลี่ยนแปลงค่าพิกเซลตามแถวหรือคอลัมน์ใด ๆ ในภาพ"
    },
    "標本化(Sampling)": {
        "question": "การสุ่มตัวอย่าง (Sampling)",
        "answer": "กระบวนการดึงค่าอนาล็อกแบบไม่ต่อเนื่องจากสัญญาณอนาล็อก (ความเข้มของแสงแบบต่อเนื่อง) ณ จุดสุ่มตัวอย่างที่จัดเรียงไว้เป็นช่วง ๆ"
    },
    "標本点(Sampling Point)": {
        "question": "จุดสุ่มตัวอย่าง (Sampling Point)",
        "answer": "ตำแหน่งที่จัดเรียงในรูปแบบตารางสม่ำเสมอในแนวตั้งและแนวนอน ซึ่งความเข้มของแสงถูกดึงออกมาเป็นค่าแรงดันไฟฟ้าระหว่างการสุ่มตัวอย่างภาพ"
    },
    "標本化間隔(Sampling Interval)": {
        "question": "ช่วงการสุ่มตัวอย่าง (Sampling Interval)",
        "answer": "ในกระบวนการสุ่มตัวอย่าง คือระยะห่างเท่ากันระหว่างจุดสุ่มตัวอย่างทั้งในแนวตั้งและแนวนอน ซึ่งสอดคล้องกับขนาดของพิกเซล"
    },
    "標本値(Sampling Value)": {
        "question": "ค่าสุ่มตัวอย่าง (Sampling Value)",
        "answer": "ค่าอนาล็อกที่จุดสุ่มตัวอย่างเอง ซึ่งส่งออกเป็นสัญญาณแรงดันไฟฟ้าอนาล็อกจากเซนเซอร์รับภาพ"
    },
    "量子化(Quantization)": {
        "question": "การควอนไทซ์ (Quantization)",
        "answer": "กระบวนการแปลงค่าสุ่มตัวอย่างอนาล็อกให้เป็นค่าตัวเลขที่มีความละเอียดจำกัด (ค่าพิกเซล) ซึ่งดำเนินการโดยตัวแปลง A/D"
    },
    "量子レベル (Quantization Level)": {
        "question": "ระดับการควอนไทซ์ (Quantization Level)",
        "answer": "จำนวนขั้นตอนที่ไม่ต่อเนื่องที่ค่าสุ่มตัวอย่างสามารถมีได้หลังจากการควอนไทซ์ ตัวอย่างเช่น การควอนไทซ์ 8 บิตให้ 256 ระดับ"
    },
    "標本化定理(Sampling Theorem)": {
        "question": "ทฤษฎีการสุ่มตัวอย่าง (Sampling Theorem)",
        "answer": "ทฤษฎีที่ระบุว่าข้อมูลในสัญญาณอนาล็อกที่ถูกจำกัดแถบความถี่สูงสุด $f_{max}$ จะไม่สูญหายหากถูกสุ่มตัวอย่างด้วยความถี่ $2f_{max}$ หรือมากกว่า"
    },
    "エイリアシング (Aliasing)": {
        "question": "เอเลียสซิ่ง (Aliasing)",
        "answer": "ปรากฏการณ์ที่สัญญาณปลอม (alias) ซึ่งแตกต่างจากสัญญาณเดิมปรากฏในค่าสุ่มตัวอย่างเมื่อเงื่อนไขของทฤษฎีการสุ่มตัวอย่างไม่เป็นไปตามที่กำหนด"
    },
    "擬似輪郭(False Contour)": {
        "question": "ขอบเขตเสมือน (False Contour)",
        "answer": "ปรากฏการณ์ที่ขอบเขตคล้ายเส้นชั้นความสูง (การเปลี่ยนแปลงค่าพิกเซลแบบขั้นบันได) ที่ไม่มีอยู่ในภาพอนาล็อกเดิมปรากฏในภาพดิจิทัลเนื่องจากข้อผิดพลาดในการควอนไทซ์"
    },
    "量子化雑音(Quantization Noise)": {
        "question": "สัญญาณรบกวนจากการควอนไทซ์ (Quantization Noise)",
        "answer": "ความผิดเพี้ยนของค่าพิกเซลที่ปรากฏในภาพดิจิทัล ซึ่งเกิดจากข้อผิดพลาดในการปัดเศษ (ข้อผิดพลาดในการควอนไทซ์) ที่สร้างขึ้นระหว่างการควอนไทซ์"
    },
    "時系列画像(Time series images)": {
        "question": "ภาพอนุกรมเวลา (Time series images)",
        "answer": "ลำดับของภาพโทนสีเทาที่จัดเรียงตามทิศทางเวลา ซึ่งเป็นผลมาจากการสุ่มตัวอย่างและการควอนไทซ์ในทิศทางเวลาที่ความถี่สอดคล้องกับอัตราเฟรม"
    },
    "階調変換関数 (Gray-level transformation function)": {
        "question": "ฟังก์ชันการแปลงระดับสีเทา (Gray-level transformation function)",
        "answer": "ฟังก์ชันที่ระบุความสัมพันธ์การแมปปิ้งระหว่างค่าพิกเซลของภาพนำเข้าและค่าพิกเซลที่สอดคล้องของภาพส่งออก"
    },
    "トーンカーブ (Tone Curve)": {
        "question": "โทนเคิร์ฟ (Tone Curve)",
        "answer": "การแสดงฟังก์ชันการแปลงระดับสีเทาด้วยกราฟ การเปลี่ยนรูปร่างของเส้นโค้งช่วยปรับความสว่างและความคมชัดของภาพด้วยสายตา"
    },
    "ガンマ変換 (Gamma Transformation)": {
        "question": "การแปลงแกมมา (Gamma Transformation)",
        "answer": "การแปลงโทนสีโดยใช้โทนเคิร์ฟแบบยกกำลัง: $y=255(\\frac{x}{255})^{\\frac{1}{\\gamma}}$ ซึ่งเปลี่ยนลักษณะการตอบสนองความสว่างของภาพตามค่า $\\gamma$."
    },
    "ヒストグラム平坦化 (Histogram Equalization)": {
        "question": "การปรับฮิสโทแกรมให้เท่ากัน (Histogram Equalization)",
        "answer": "วิธีการแก้ไขการกระจายที่ไม่สม่ำเสมอของฮิสโทแกรมของภาพโดยอัตโนมัติ โดยการทำให้มันแบนราบ ซึ่งเป็นการปรับปรุงความคมชัดของภาพโดยรวม"
    },
    "疑似カラー (Pseudo Color)": {
        "question": "สีเทียม (Pseudo Color)",
        "answer": "กระบวนการใช้สีเทียมกับภาพโทนสีเทาโดยใช้ค่าพิกเซลเป็นค่าของช่องสัญญาณ R, G, และ B และใช้โทนเคิร์ฟที่แตกต่างกันอย่างเหมาะสมกับแต่ละช่องสัญญาณ"
    },
    "画像間演算 (Inter-image Operation)": {
        "question": "การดำเนินการระหว่างภาพ (Inter-image Operation)",
        "answer": "การดำเนินการที่ดำเนินการกับภาพนำเข้าตั้งแต่สองภาพขึ้นไป โดยที่การคำนวณที่กำหนดไว้จะดำเนินการแบบองค์ประกอบต่อองค์ประกอบ (พิกเซลต่อพิกเซล) ในตำแหน่งเดียวกันทั่วทั้งภาพ"
    },
    "アルファブレンディング (Alpha Blending)": {
        "question": "การผสมแบบอัลฟา (Alpha Blending)",
        "answer": "กระบวนการรวมสองภาพเข้าด้วยกันโดยใช้ปัจจัยน้ำหนัก $(\\alpha, \text{ โดยที่ } 0\\le \\alpha \\le 1)$ เพื่อปรับการมีส่วนร่วมของค่าพิกเซลของแต่ละภาพ"
    },
    "ディゾルブ (Dissolve)": {
        "question": "การละลายภาพ (Dissolve)",
        "answer": "เทคนิคในวิดีโอที่ค่าของ $\\alpha$ ถูกเปลี่ยนแปลงตามเวลาเพื่อเปลี่ยนจากฉากหนึ่งไปยังอีกฉากหนึ่งอย่างค่อยเป็นค่อยไป"
    },
    "オーバーラップ (Overlap)": {
        "question": "การซ้อนทับ (Overlap)",
        "answer": "คำที่มักใช้เหมือนกับ 'การละลายภาพ' เพื่ออ้างถึงวิธีการซ้อนทับฉากวิดีโอตามเวลาเพื่อเปลี่ยนระหว่างฉากเหล่านั้น"
    },
    "フェード (Fade)": {
        "question": "การเลือนภาพ (Fade)",
        "answer": "ประเภทของการละลายภาพที่เปลี่ยนผ่านหน้าจอสีดำหรือสีขาวที่เป็นสีสม่ำเสมอโดยเฉพาะ"
    },
    "マスク処理 (Mask Operation)": {
        "question": "การดำเนินการมาสก์ (Mask Operation)",
        "answer": "กระบวนการรวมสองภาพเข้าด้วยกันโดยใช้ภาพมาสก์เพื่อระบุ พิกเซลต่อพิกเซล ว่าส่วนใดควรนำมาจากภาพต้นฉบับใด"
    },
    "マスク画像 (Mask Image)": {
        "question": "ภาพมาสก์ (Mask Image)",
        "answer": "ภาพ (โดยทั่วไปสร้างโดยใช้ค่า 1 หรือ 0) ที่เตรียมไว้ล่วงหน้าเพื่อระบุ พิกเซลต่อพิกเซล ว่าส่วนใดของภาพต้นฉบับควรถูกใช้ในการประกอบสุดท้าย"
    },
    "マスク合成 (Mask Compositing)": {
        "question": "การจัดองค์ประกอบมาสก์ (Mask Compositing)",
        "answer": "มีความหมายเหมือนกันกับ 'การดำเนินการมาสก์' ซึ่งหมายถึงการรวมภาพตามข้อมูลมาสก์เพื่อกำหนดและรวมขอบเขตเบื้องหน้าและพื้นหลังเข้าด้วยกันอย่างชัดเจนในภาพประกอบสุดท้าย"
    },
    "可視光 (Visible Light)": {
        "question": "แสงที่มองเห็นได้ (Visible Light)",
        "answer": "คลื่นแม่เหล็กไฟฟ้าในช่วงความยาวคลื่นที่มนุษย์สามารถรับรู้ได้ (ช่วงของแสงที่มองเห็นได้ด้วยตามนุษย์)"
    },
    "紫外線(Ultraviolet Ray)": {
        "question": "รังสีอัลตราไวโอเลต (Ultraviolet Ray)",
        "answer": "คลื่นแม่เหล็กไฟฟ้าที่มีความยาวคลื่นสั้นกว่าสีม่วงที่รับรู้ได้ ซึ่งมนุษย์ไม่สามารถรับรู้ได้"
    },
    "赤外線(Infrared Ray)": {
        "question": "รังสีอินฟราเรด (Infrared Ray)",
        "answer": "คลื่นแม่เหล็กไฟฟ้าที่มีความยาวคลื่นยาวกว่าสีแดงที่รับรู้ได้ ซึ่งมนุษย์ไม่สามารถรับรู้ได้"
    },
    "混色 (Colour Mixing)": {
        "question": "การผสมสี (Colour Mixing)",
        "answer": "กระบวนการผสมสี ซึ่งรวมถึงสองประเภท: การผสมสีแบบบวก (Additive Colour Mixing) และการผสมสีแบบลบ (Subtractive Colour Mixing)"
    },
    "加法混色 (Additive Colour Mixing)": {
        "question": "การผสมสีแบบบวก (Additive Colour Mixing)",
        "answer": "กระบวนการผสมแสงสีต่าง ๆ เพื่อสร้างสีใหม่"
    },
    "減法混色 (Subtractive Colour Mixing)": {
        "question": "การผสมสีแบบลบ (Subtractive Colour Mixing)",
        "answer": "ปรากฏการณ์ที่สีมืดลงเมื่อมีการผสมสารสี เช่น สีทาและหมึก"
    },
    "RGBカラー画像(RGB Color Image)": {
        "question": "ภาพสีแบบ RGB (RGB Color Image)",
        "answer": "ภาพสีที่มีค่าพิกเซลสามค่า (สีแดง สีเขียว สีน้ำเงิน) ที่สอดคล้องกับตำแหน่งในภาพ"
    },
    "ヒストグラム (Histogram)": {
        "question": "ฮิสโทแกรม (Histogram)",
        "answer": "กราฟแท่งที่แสดงการกระจายของค่าพิกเซล โดยที่แกนนอนเป็นค่าพิกเซลและแกนตั้งเป็นความถี่ (จำนวน) ของพิกเซลที่มีค่านั้น"
    },
    "最小値・最大値 (Minimum/Maximum Value)": {
        "question": "ค่าต่ำสุด/ค่าสูงสุด (Minimum/Maximum Value)",
        "answer": "ในค่าพิกเซลของภาพ ค่าที่เล็กที่สุดเรียกว่าค่าต่ำสุด และค่าที่ใหญ่ที่สุดเรียกว่าค่าสูงสุด"
    },
    "平均値(Mean)": {
        "question": "ค่าเฉลี่ย (Mean Value)",
        "answer": "ค่าเฉลี่ยของภาพขนาด $M \\times N$ พิกเซล คำนวณโดยผลรวมของค่าพิกเซลทั้งหมดหารด้วยจำนวนพิกเซลทั้งหมด: $Mean=\\frac{1}{M\\times N}\\sum_{x=0}^{M-1}\\sum_{y=0}^{N-1}p(x,y)$."
    },
    "中央値 (Median)": {
        "question": "ค่ามัธยฐาน (Median Value)",
        "answer": "กำหนดจากฮิสโทแกรมของภาพ เป็นค่าพิกเซลที่ตำแหน่งที่ $MN/2$ เมื่อจัดเรียงจากค่าพิกเซลที่เล็กที่สุด"
    },
    "最頻値 (Mode)": {
        "question": "ค่าฐานนิยม (Mode Value)",
        "answer": "ค่าพิกเซลที่มีความถี่สูงสุด (จำนวนสูงสุด) เมื่อกำหนดจากฮิสโทแกรมของภาพ"
    },
    "分散 (Variance)": {
        "question": "ความแปรปรวน (Variance)",
        "answer": "ความแปรปรวนของภาพขนาด $M \\times N$ พิกเซล คำนวณโดยสูตร: $\\sigma^{2}=\\frac{1}{M\\times N}\\sum_{i=1}^{M}\\sum_{j=1}^{N}p_{ij}^{2}-(\\frac{1}{M\\times N}\\sum_{i=1}^{M}\\sum_{j=1}^{N}p_{ij})^{2}$."
    },
    "6角錐モデル - HSV (Hexcone Model - HSV)": {
        "question": "แบบจำลองหกเหลี่ยมพีระมิด - HSV (Hexcone Model - HSV)",
        "answer": "การแสดงภาพ 3 มิติของแบบจำลองสี HSV ซึ่งแสดงสีโดยใช้องค์ประกอบสามอย่าง: สี (Hue), ความอิ่มตัว (Saturation), และความสว่าง (Value) ในรูปทรงหกเหลี่ยมพีระมิด"
    },
    "空間フィルタリング/空間フィルタ (Spatial Filtering / Spatial Filter)": {
        "question": "การกรองเชิงพื้นที่/ตัวกรองเชิงพื้นที่ (Spatial Filtering / Spatial Filter)",
        "answer": "กระบวนการคำนวณค่าของพิกเซลเดียวในภาพส่งออกโดยใช้ค่าพิกเซลภายในพื้นที่ของภาพนำเข้า ซึ่งรวมถึงพิกเซลที่สอดคล้องและพิกเซลรอบข้าง ตัวกรองที่ใช้เรียกว่าตัวกรองเชิงพื้นที่"
    },
    "線形フィルタ (Linear Filter)": {
        "question": "ตัวกรองเชิงเส้น (Linear Filter)",
        "answer": "ตัวกรองเชิงพื้นที่ประเภทหนึ่งที่คำนวณพิกเซลส่งออกหนึ่งพิกเซลเป็นผลรวมแบบถ่วงน้ำหนักของพิกเซลรอบข้างหลายพิกเซล โดยใช้สูตร: $g(i,j)=\\sum_{m=-W}^{W}\\sum_{n=-W}^{W}f(i+m,j+n)h(m,n)$."
    },
    "非線形フィルタ (Nonlinear Filter)": {
        "question": "ตัวกรองไม่เชิงเส้น (Nonlinear Filter)",
        "answer": "ตัวกรองใด ๆ ที่เกี่ยวข้องกับการประมวลผลที่ไม่สอดคล้องกับขั้นตอนตัวกรองเชิงเส้น ซึ่งแตกต่างจากตัวกรองเชิงเส้นตรงที่ไม่เป็นไปตามหลักการซ้อนทับ ทำให้สามารถประมวลผลที่ซับซ้อนยิ่งขึ้นได้"
    },
    "平滑化(Smoothing)": {
        "question": "การทำให้เรียบ (Smoothing)",
        "answer": "กระบวนการที่ทำให้เกิดการเปลี่ยนแปลงโทนสีที่ราบรื่นกับภาพ คล้ายกับภาพที่ไม่อยู่ในโฟกัส นอกจากนี้ยังใช้เพื่อลดความผันผวนของโทนสีที่ไม่ต้องการ เช่น สัญญาณรบกวน"
    },
    "平均化フィルタ (Averaging Filter)": {
        "question": "ตัวกรองค่าเฉลี่ย (Averaging Filter)",
        "answer": "ตัวกรองที่คำนวณค่าเฉลี่ยของค่าพิกเซลภายในพื้นที่ที่ครอบคลุมโดยตัวกรอง ตัวอย่าง: ตัวกรอง $3\\times3$ พิกเซลที่สัมประสิทธิ์ทั้งหมดคือ $1/9$."
    },
    "重み付き平均化/加重平均化フィルタ (Weighted Averaging / Weighted Averaging Filter)": {
        "question": "ตัวกรองค่าเฉลี่ยถ่วงน้ำหนัก (Weighted Averaging / Weighted Averaging Filter)",
        "answer": "การหาค่าเฉลี่ยโดยใช้ตัวกรองที่ 'ยิ่งใกล้กับพิกเซลเอง (จุดศูนย์กลางของตัวกรอง) น้ำหนักยิ่งมาก และยิ่งไกลออกไป น้ำหนักยิ่งน้อย' (ตัวกรองค่าเฉลี่ยถ่วงน้ำหนัก)"
    },
    "ガウシアンフィルタ (Gaussian Filter)": {
        "question": "ตัวกรองเกาส์เซียน (Gaussian Filter)",
        "answer": "ตัวกรองค่าเฉลี่ยถ่วงน้ำหนักประเภทหนึ่งที่น้ำหนักจะขึ้นอยู่กับการกระจายเกาส์เซียน สูตรการกระจายเกาส์เซียน 2 มิติคือ: $h_{\\epsilon}(x,y)=\\frac{1}{2\\pi\\sigma^{2}}exp(-\\frac{x^{2}+y^{2}}{2\\sigma^{2}})$."
    },
    "特定方向への平滑化 (Smoothing in a Specific Direction)": {
        "question": "การทำให้เรียบในทิศทางเฉพาะ (Smoothing in a Specific Direction)",
        "answer": "เทคนิคการกรองที่ใช้ในการประมวลผลภาพเพื่อลดสัญญาณรบกวนหรือเบลอเฉพาะตามทิศทางที่เลือก (เช่น แนวนอน แนวตั้ง หรือแนวทแยง)"
    },
    "エッジ抽出 (Edge Extraction)": {
        "question": "การแยกขอบ (Edge Extraction)",
        "answer": "กระบวนการดึงส่วนขอบที่ความสว่างเปลี่ยนแปลงอย่างกะทันหันในภาพ"
    },
    "微分フィルタ (Derivative Filter)": {
        "question": "ตัวกรองอนุพันธ์ (Derivative Filter)",
        "answer": "ในภาพดิจิทัล อนุพันธ์จะถูกแทนที่ด้วยความแตกต่างระหว่างพิกเซลเป้าหมายและพิกเซลที่อยู่ติดกัน ตัวอย่างตัวกรอง (ค่าเฉลี่ยความแตกต่างซ้าย/ขวา): $\\begin{pmatrix} 0 & 0 & 0 \\\\ -1/2 & 0 & 1/2 \\\\ 0 & 0 & 0 \\end{pmatrix}$."
    },
    "プリューウィットフィルタ (Prewitt Filter)": {
        "question": "ตัวกรองพรีวิตต์ (Prewitt Filter)",
        "answer": "ตัวกรองที่รวมการหาอนุพันธ์ในแนวนอนและการทำให้เรียบในแนวตั้ง (เช่น การหาค่าเฉลี่ยพิกเซล 3 พิกเซลในแนวตั้ง) เพื่อแยกขอบในขณะที่ลดสัญญาณรบกวน ตัวอย่างตัวเลขของตัวกรองแนวนอน: $\\begin{pmatrix} -1 & 0 & 1 \\\\ -1 & 0 & 1 \\\\ -1 & 0 & 1 \\end{pmatrix}$."
    },
    "ソーベルフィルタ (Sobel Filter)": {
        "question": "ตัวกรองโซเบล (Sobel Filter)",
        "answer": "คล้ายกับตัวกรองพรีวิตต์ โดยรวมการหาอนุพันธ์และการทำให้เรียบ แต่ใช้การหาค่าเฉลี่ยถ่วงน้ำหนักระหว่างการทำให้เรียบในแนวตั้ง ตัวอย่างตัวเลขของตัวกรองแนวนอน: $\\begin{pmatrix} -1 & 0 & 1 \\\\ -2 & 0 & 2 \\\\ -1 & 0 & 1 \\end{pmatrix}$."
    },
    "2次微分フィルタ (Second Derivative Filter)": {
        "question": "ตัวกรองอนุพันธ์อันดับสอง (Second Derivative Filter)",
        "answer": "กระบวนการที่ทำซ้ำการหาอนุพันธ์สองครั้ง (ทำซ้ำการหาความแตกต่างสองครั้ง) สิ่งนี้ให้ 'ขนาดของการเปลี่ยนแปลงค่าพิกเซล' ซึ่งช่วยให้สามารถรับขอบได้อย่างแม่นยำกว่าการใช้อนุพันธ์อันดับแรก"
    },
    "ラプラシアンフィルタ (Laplacian Filter)": {
        "question": "ตัวกรองลาปลาเซียน (Laplacian Filter)",
        "answer": "ตัวกรองเดียวที่เทียบเท่ากับกระบวนการบวกผลลัพธ์ของอนุพันธ์อันดับสองในแนวนอนและอนุพันธ์อันดับสองในแนวตั้ง ตัวอย่าง: $\\begin{pmatrix} 0 & 1 & 0 \\\\ 1 & -4 & 1 \\\\ 0 & 1 & 0 \\end{pmatrix}$."
    },
    "エッジ検出(Edge Detection)": {
        "question": "การตรวจจับขอบ (Edge Detection)",
        "answer": "การประมวลผลเพิ่มเติมที่ดำเนินการเพื่อระบุว่าพิกเซลใดในภาพส่งออกที่มีค่าเป็นจำนวนจริงจากการกรองเชิงพื้นที่สอดคล้องกับขอบ"
    },
    "鮮鋭化(Sharpening)": {
        "question": "การเพิ่มความคมชัด (Sharpening)",
        "answer": "กระบวนการที่เพิ่มขอบในขณะที่ยังคงรักษาสีโทนเดิมของภาพไว้ เป็นการแปลงที่ตรงข้ามกับการทำให้เรียบ โดยเพิ่มการเปลี่ยนแปลงค่าพิกเซล (การเปลี่ยนแปลงโทนสี) ของภาพเดิม"
    },
    "メディアンフィルタ (Median Filter)": {
        "question": "ตัวกรองมัธยฐาน (Median Filter)",
        "answer": "ตัวกรองที่ส่งออกค่ามัธยฐาน (ค่ากลาง) ภายในพื้นที่ที่กำหนด แทนที่จะเป็นค่าเฉลี่ยของค่าพิกเซล มีประสิทธิภาพสูงในการกำจัดสัญญาณรบกวนแบบเดือยแหลม (spike-like noise)"
    },
    "最大値フィルタ (Maximum Value Filter)": {
        "question": "ตัวกรองค่าสูงสุด (Maximum Value Filter)",
        "answer": "ตัวกรองที่เปรียบเทียบค่าพิกเซลรอบข้างและแทนที่ค่าพิกเซลด้วยค่าที่ใหญ่ที่สุดในบรรดาค่าเหล่านั้น มีประสิทธิภาพในการกำจัดสัญญาณรบกวนที่สว่าง (จุดสีขาว) และถูกเรียกว่าตัวกรองการขยาย (dilation) ด้วย"
    },
    "最小値フィルタ (Minimum Value Filter)": {
        "question": "ตัวกรองค่าต่ำสุด (Minimum Value Filter)",
        "answer": "ตัวกรองที่เปรียบเทียบค่าพิกเซลรอบข้างและแทนที่ค่าพิกเซลด้วยค่าที่เล็กที่สุดในบรรดาค่าเหล่านั้น มีประสิทธิภาพในการกำจัดสัญญาณรบกวนที่มืด (จุดสีดำ) และถูกเรียกว่าตัวกรองการหดตัว (erosion) ด้วย"
    }
}