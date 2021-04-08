using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System;
using System.Linq;
using System.IO;
using TMPro;
using UnityEditor;

public class MarbleTracks : MonoBehaviour
{
    public Shader _drawShader;
    private Material _sandMaterial, _drawMaterial;
    private RenderTexture _splatmap;
    public GameObject _terrain;
    public Transform _marble;
    RaycastHit _groundHit;
    int _layerMask;
    [Range(1, 3)]
    public float _brushSize;
    [Range(0, 1)]
    public float _brushStrength;

    public float _;
    public float _scale;
    int count;
    private List<int[]> moves;

    float t;
    Vector3 startPosition;
    Vector3 target;
    float timeToReachTarget;
    public float _time;

    public UnityEngine.Object GCodeFile;

    private List<int[]> ReadGCode()
    {
        List<int[]> sequence = new List<int[]>();
        String gcode_src = AssetDatabase.GetAssetPath(GCodeFile);
        FileInfo fread = new FileInfo(gcode_src);
        StreamReader reader = fread.OpenText();
        string text = " ";

        while (text != null)
        {
            text = reader.ReadLine();
            if (text != null)
            {
                if (text.Contains("X"))
                {
                    string xsub = text.Substring(text.LastIndexOf("X")+1, text.LastIndexOf("Y")-(text.LastIndexOf("X")+1));
                    string ysub = text.Substring(text.LastIndexOf("Y") + 1, text.Length - (text.LastIndexOf("Y") + 1));
                    sequence.Add(new int[2] { Int32.Parse(ysub), Int32.Parse(xsub) });
                }
            }
        }
        reader.Close();

        return sequence;
    }

    // Start is called before the first frame update
    void Start()
    {

        moves = ReadGCode();

        _layerMask = LayerMask.GetMask("Ground");
        _drawMaterial = new Material(_drawShader);
        _sandMaterial = _terrain.GetComponent<MeshRenderer>().material;
        _sandMaterial.SetTexture("_Splat", _splatmap = new RenderTexture(1024, 1024, 0, RenderTextureFormat.ARGBFloat));

        InvokeRepeating("SetNextMove", 1.0f, _time);

        startPosition = target = transform.position;
        count = 0;
    }

    // Update is called once per frame
    void Update()
    {
        t += Time.deltaTime / timeToReachTarget;
        if (count < moves.Count)
        {
            transform.position = Vector3.Lerp(startPosition, target, Time.deltaTime);
        } else if (count == moves.Count)
        {
            transform.position = Vector3.Lerp(startPosition, target, Time.deltaTime);
            count++;
        } else
        {
            transform.position = Vector3.Lerp(startPosition, transform.position, 0.0f);
        }
        //transform.position = Vector3.MoveTowards(startPosition, target, 0.1f);

        if (Physics.Raycast(_marble.position, -Vector3.up, out _groundHit, 1f, _layerMask))
        {
            _drawMaterial.SetVector("_Coordinate", new Vector4(_groundHit.textureCoord.x, _groundHit.textureCoord.y, 0, 0));
            _drawMaterial.SetFloat("_Strength", _brushStrength);
            _drawMaterial.SetFloat("_Size", _brushSize);
            RenderTexture temp = RenderTexture.GetTemporary(_splatmap.width, _splatmap.height, 0, RenderTextureFormat.ARGBFloat);
            Graphics.Blit(_splatmap, temp);
            Graphics.Blit(temp, _splatmap, _drawMaterial);
            RenderTexture.ReleaseTemporary(temp);
        }
    }

    public void SetNextMove()
    {
        if (moves != null)
        {
            if (count < moves.Count)
            {
                t = 0;
                startPosition = transform.position;
                timeToReachTarget = _time;
                target = new Vector3(transform.position.x + (moves[count][1] * _scale), transform.position.y, transform.position.z - (moves[count][0] * _scale));
                count++;
            }
        }
        

    }
}
